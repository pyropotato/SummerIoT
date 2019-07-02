	
#!/usr/bin/python
import sys
import Adafruit_DHT
import datetime
import csv

try:
    while True:
        row = []
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        #print (str(temperature) + 'C')
        #print (str(humidity) + '%')
        #print ('')
        #print('Temp:{0:0.1f}C, Humidity:{1:0.1f} %'.format(temperature,humidity))
        #print(datetime.datetime.now())
        #print('')
        row.append(temperature)
        row.append(humidity)
        row.append(str(datetime.datetime.now()))
        print(row)
        with open('reading.csv','a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)

finally:
    csvFile.close()
