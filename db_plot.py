import matplotlib.pyplot as plt
import csv
import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('new.db')
c = conn.cursor()

x = []
y = []
z = []

c.execute('SELECT * FROM iot')
data = c.fetchall()

for row in data:
    x.append(row[0])
    y.append(row[2])
    z.append(row[3])

plt.subplot(121)
plt.plot(x,y, label = 'Temp')
plt.xlabel('Count')
plt.ylabel('C')
plt.title('Temperature')
plt.legend()
plt.subplot(122)
plt.plot(x,z,label = 'Humi')
plt.xlabel('Count')
plt.ylabel('%')
plt.title('Humidity')
plt.legend()
plt.show()
