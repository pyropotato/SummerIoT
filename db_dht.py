import sys
import Adafruit_DHT
import datetime
import sqlite3
import time

conn = sqlite3.connect('new.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS iot(`COUNT` INTEGER PRIMARY KEY AUTOINCREMENT,`TIMESTAMP` TEXT NOT NULL, `TEMP` REAL, `HUM` REAL)")

def dynamic_data_entry(temp,hum):
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d-%M-%S'))
    c.execute("INSERT INTO iot(TIMESTAMP,TEMP,HUM)VALUES(?, ?, ?)",(date,temp,hum))
    conn.commit()
    print(date)
    print(temp)
    print(hum)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        dynamic_data_entry(temperature,humidity)

finally:
    c.close()
    conn.close()
