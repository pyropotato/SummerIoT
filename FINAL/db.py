import sys
import datetime
import paho.mqtt.client as mqtt
import pymysql
db = pymysql.connect("localhost","root","tabletop97","iot" )

HOST = "192.168.43.205"
client = mqtt.Client()

temp = 0
hum = 0

def on_connect(client,userdata,flags,rc):
    print("Connected: " + str(rc))
    client.subscribe("final/room/temp")
    client.subscribe("final/room/hum")

def on_message(client,userdata,msg):
    global temp
    global hum
    topic = msg.topic.split("/")[2]
    if topic == "temp":
        temp = float(msg.payload.decode())
        print("temp =" + str(temp))

    elif topic == "hum":
        hum = msg.payload.decode()
        print("hum =" + str(hum))

    try:
        cursor = db.cursor()
        sql = "INSERT INTO FINAL (TEMP,HUM) VALUES (%f,%f)"%(float(temp),float(hum))
        #print(sql)
        cursor.execute(sql)
        db.commit()

    except Exception as e:
        print("Exeception occured:{}".format(e))

try:
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST,1883,20)
    client.loop_forever()

finally:
    db.close()
