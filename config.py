import sqlite3

conn = sqlite3.connect('customer.db')

# create a new cursor
crs = conn.cursor()
