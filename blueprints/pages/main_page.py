from flask import Blueprint, request, jsonify
from models.default import GetData, GetPeriodData
from crud import table_handler
from core.db import get_connection
from core.data_inserting import data_insert, data_list
import threading
from parcers.currency import currency
from core.errors.secondary_data import bank_names
# from core.errors.common import (
#     if_json_exists,
#     if_bank_name_correct,
#     if_currency_name_correct,
# )


main_page_blueprint = Blueprint("main_page_blueprint", __name__)


thread1 = threading.Thread(
    target=data_insert.insert_data, args=(data_list,), daemon=True
)


@main_page_blueprint.route("/", methods=["POST"])
def start_thread_for_data():
    if thread1.is_alive() is True:
        return jsonify(error="You can't start more than 1 thread")
    thread1.start()
    return jsonify(info="Thread was started")
    # while True:
    #     print(thread1.is_alive())
    #     sleep(10)


@main_page_blueprint.route("/", methods=["DELETE"])
def stop_thread():
    if thread1.is_alive() is False:
        return jsonify(error="You can't stop thread, that is already disabled")
    data_insert.indicator == 1
    return jsonify(info="Thread was stopped")


@main_page_blueprint.route("/newest")
def get_info_newest():
    if request.json is None:
        return jsonify(error="Json is not found")
    request_data = GetData(**request.json)
    if_bank_name_correct(request_data)

    with get_connection() as conn:
        data = table_handler.get_newest_data(conn=conn, db=request_data.bank)
        return jsonify(data[0], data[1], data[2])


@main_page_blueprint.route("/all")
def get_info_all():
    with get_connection() as conn:
        data = table_handler.get_data_from_all(conn=conn)
        return jsonify(data)


@main_page_blueprint.route("/period")
def get_info_by_period():
    if request.json is None:
        return jsonify(error="Json is not found")
    request_data = GetPeriodData(**request.json)

    if request_data.bank not in bank_names:
        return jsonify(
            error="Bank name is incorrect. Try using PrivatBank, Ukrsibbank or KitGroup"
        )

    if request_data.currency not in currency.values():
        return jsonify(
            error="No such currency has been found. Try using USD, EUR or RUB"
        )
    
    with get_connection() as conn:
        data = table_handler.get_data_by_period(
            conn=conn, data=request_data, db=request_data.bank
        )
        return jsonify(data)
