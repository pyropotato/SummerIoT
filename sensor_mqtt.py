
#!/usr/bin/python
import sys
import Adafruit_DHT
import datetime
import csv
import paho.mqtt.client as mqtt #import the client1
broker_address="test.mosquitto.org"
client = mqtt.Client("P1") #create new instance
client.connect(broker_address,1883,60) #connect to broker
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
        client.publish("summeriot/temp",str(temperature))#publish
        client.publish("summeriot/hum",str(humidity))#publish
        row.append(temperature)
        row.append(humidity)
        row.append(str(datetime.datetime.now()))
        print(row)
        with open('reading.csv','a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)

finally:
    csvFile.close()
    client.disconnect()
