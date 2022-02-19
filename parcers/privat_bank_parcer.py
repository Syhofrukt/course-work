from .currency import currency

import requests


class Privatbank_parcer:
    __url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    __name = "PrivatBank"

    def __get_json(self):
        response = requests.get(self.__url)
        return response.json()

    def get_name(self):
        return self.__name

    def get_currency_rate(self):
        currency_rate = {"rate": []}
        result = self.__get_json()
        for line in result:
            name = line["ccy"].strip().lower()
            if name in currency.keys():
                currency_rate["rate"].append(
                    {
                        "currency_name": currency[name],
                        "value_buy": round(float(line["buy"]), 2),
                        "value_sale": round(float(line["sale"]), 2),
                    }
                )
        return currency_rate


if __name__ == "__main__":
    from pprint import pprint

    bank = Privatbank_parcer()
    pprint(bank.get_currency_rate())
