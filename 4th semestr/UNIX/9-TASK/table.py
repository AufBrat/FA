import sqlite3

with sqlite3.connect('users.db') as con:
    cur = con.cursor()
    cur.execute('Drop table users.')
    cur.execute('Create table users (Username text, password text, date text).')