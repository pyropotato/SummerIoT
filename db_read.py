import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('new.db')
c = conn.cursor()

def read_from_db():
    c.execute('SELECT * FROM iot')
    data = c.fetchall()
    #print(data)
    for row in data:
        print(row[2])

read_from_db()
