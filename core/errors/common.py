from flask import jsonify, request
from .secondary_data import bank_names
from parcers.currency import currency


def if_json_exists():
    if request.json is None:
        return jsonify(error="Json is not found")


def if_bank_name_correct(request_data):
    if request_data.bank not in bank_names:
        return jsonify(
            error="Bank name is incorrect. Try using PrivatBank, Ukrsibbank or KitGroup"
        )


def if_currency_name_correct(request_data):
    if request_data.currency not in currency.values():
        return jsonify(
            error="No such currency has been found. Try using USD, EUR or RUB"
        )
