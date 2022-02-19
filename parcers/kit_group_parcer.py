import requests
from bs4 import BeautifulSoup
from .currency import currency


class Kit_group_parcer:
    __url = "https://obmenka.od.ua/"
    __name = "KitGroup"

    def __get_html(self):
        response = requests.get(self.__url)
        return response.text

    def get_name(self):
        return self.__name

    def get_currency_rate(self):
        currency_rate = {"rate": []}

        html = self.__get_html()
        soup = BeautifulSoup(html, "lxml")
        content = soup.find_all("li", class_="currencies__block")
        for line in content:
            name = (
                line.find("div", class_="currencies__block-name")
                .find("a")
                .text.split()[1]
            )

            if (
                not name.upper().endswith("/UAH")
                or name[:3].lower() not in currency.keys()
            ):
                continue

            currency_name = currency[name[:3].lower()]
            value_buy = (
                line.find("div", class_="currencies__block-buy")
                .find("div", class_="currencies__block-num")
                .text.strip()
            )
            value_sale = (
                line.find("div", class_="currencies__block-sale")
                .find("div", class_="currencies__block-num")
                .text.strip()
            )

            currency_rate["rate"].append(
                {
                    "currency_name": currency_name,
                    "value_buy": round(float(value_buy), 2),
                    "value_sale": round(float(value_sale), 2),
                }
            )
        return currency_rate


if __name__ == "__main__":
    from pprint import pprint

    bank = Kit_group_parcer()
    pprint(bank.get_currency_rate())
