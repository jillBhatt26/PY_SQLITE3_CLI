from config import *

def create_table():
    crs.execute("""CREATE TABLE IF NOT EXISTS customers (
        f_name TEXT NOT NULL,
        l_name TEXT NOT NULL,
        email TEXT NOT NULL
    )""")

    conn.commit()

create_table()