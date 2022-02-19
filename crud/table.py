import sqlite3

from flask import jsonify


class TableHandler:
    def rows_to_dict(self, cur):
        rows = cur.fetchall()
        data = []
        for row in rows:
            metadata = {}
            for i, col in enumerate(cur.description):
                metadata[col[0]] = row[i]
            data.append(metadata)
        return data

    def create(self, data: list, conn: sqlite3.Connection):
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO {} (currency_name, value_buy, value_sale, value_date) VALUES(?, ?, ?, ?)".format(
                data[0]
            ),
            (
                data[1],
                data[2],
                data[3],
                data[4],
            ),
        )
        conn.commit()

    def get_data_from_all(self, conn: sqlite3.Connection):
        cur = conn.cursor()
        cur.execute("SELECT * FROM PrivatBank ")
        conn.commit()
        info = []
        info.append("PrivatBank")
        info.append(self.rows_to_dict(cur))

        cur.execute("SELECT * FROM Ukrsibbank ")
        conn.commit()
        info.append("Ukrsibbank")
        info.append(self.rows_to_dict(cur))

        cur.execute("SELECT * FROM KitGroup ")
        conn.commit()
        info.append("KitGroup")
        info.append(self.rows_to_dict(cur))
        return info

    def get_data_by_period(self, data, conn: sqlite3.Connection, db: str):
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM {} WHERE value_date BETWEEN ? AND ? AND currency_name = ?".format(
                db
            ),
            (
                data.date_from,
                data.date_to,
                data.currency,
            ),
        )
        conn.commit()
        data = self.rows_to_dict(cur)
        try:
            data.pop()
        except IndexError:
            raise ValueError("No data for such timedelta found")
        return data

    def get_newest_data(self, conn: sqlite3.Connection, db: str):
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM {} ORDER BY value_date DESC LIMIT 3".format(
                db,
            )
        )
        conn.commit()
        return self.rows_to_dict(cur)
