from .privat_bank_parcer import Privatbank_parcer
from .ukrsib_parcer import Ukrsib_parcer
from .kit_group_parcer import Kit_group_parcer
from datetime import datetime

banks = [Privatbank_parcer(), Ukrsib_parcer(), Kit_group_parcer()]


def get_bank_currency_info():
    currency_info_list = []
    for bank in banks:
        bank_list = []
        bank_list.append(bank.get_name())
        rates = bank.get_currency_rate()["rate"]
        for rate in rates:
            bank_list.append(
                {
                    "currency_name": rate["currency_name"],
                    "value_buy": rate["value_buy"],
                    "value_sale": rate["value_sale"],
                    "value_date": str(datetime.now().strftime("%d-%m-%Y %H:%M")),
                }
            )
        currency_info_list.append(bank_list)
    return currency_info_list
