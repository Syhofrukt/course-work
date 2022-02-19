from time import sleep
from crud import table_handler
from parcers import get_bank_currency_info
from core.db import get_connection

data_list = get_bank_currency_info()


class DataInsert:
    def __init__(self) -> None:
        self.indicator = 0

    def insert_data(self, list: list):
        self.indicator == 0
        while True:
            with get_connection() as conn:
                for sublist in list:
                    bank_name = sublist[0]
                    for element in sublist[1:]:
                        lst = [el for el in element.values()]
                        lst.insert(0, bank_name)
                        table_handler.create(data=lst, conn=conn)
            if self.indicator == 1:
                break
            sleep(60)


data_insert = DataInsert()
