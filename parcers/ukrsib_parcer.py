import requests
from bs4 import BeautifulSoup

import re
from .currency import currency


class Ukrsib_parcer:
    __url = "https://my.ukrsibbank.com/ru/personal/"
    __name = "Ukrsibbank"

    def __get_html(self):
        response = requests.get(self.__url)
        return response.text

    def get_name(self):
        return self.__name

    def get_currency_rate(self):
        currency_rate = {"rate": []}

        html = self.__get_html()
        soup = BeautifulSoup(html, "lxml")
        content = soup.find_all("div", id=re.compile("^NAL*"))
        for line in content:
            currency_name = None
            for key, value in currency.items():
                if key in line["id"].lower():
                    currency_name = value
                    break
            if currency_name is None:
                continue

            currency_rate["rate"].append(
                {
                    "currency_name": currency_name,
                    "value_buy": round(
                        float(
                            line.find("div", class_="rate__buy").find("p").text.strip()
                        ),
                        2,
                    ),
                    "value_sale": round(
                        float(
                            line.find("div", class_="rate__sale").find("p").text.strip()
                        ),
                        2,
                    ),
                }
            )
        return currency_rate


if __name__ == "__main__":
    from pprint import pprint

    bank = Ukrsib_parcer()
    pprint(bank.get_currency_rate())
