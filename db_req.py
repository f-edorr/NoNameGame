import sqlite3


class DbReq:
    def get_data(self, column, table, condition, count):
        with sqlite3.connect("db.db") as con:
            cur = con.cursor()
            cur.execute(f"""SELECT {column} FROM {table} {condition}""")
            if count == -1:
                data = cur.fetchall()
            else:
                data = cur.fetchmany(count)

            cur.close()
        return data

    def write_data(self, table, *values):
        s = '?, ' * len(values)
        s = s[:-2]
        with sqlite3.connect("db.db") as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO {table} VALUES({s});", values)
            con.commit()
            cur.close()

    def update_data(self):
        pass
