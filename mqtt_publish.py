#mqtt publish demo
import paho.mqtt.client as mqtt
import datetime
import sys
import Adafruit_DHT
import csv

broker_address = "test.mosquitto.org"
client = mqtt.Client("PI")
client.connect(broker_address,1883,60)

try :
    while True:
        row = []
        humidity, tempreature = Adafruit_DHT.read_retry(11,4)
        row.append(tempreature)
        row.append(humidity)
        row.append(str(datetime.datetime.now()))
        client.publish("core/temp",str(tempreature))
        client.publish("core/humidity",str(humidity))
        print(row)
        with open('data4.csv','a') as writeFile :
            writer = csv.writer(writeFile)
            writer.writerow(row)
finally :
writeFile.close()
