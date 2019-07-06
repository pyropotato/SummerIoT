import serial
import RPi.GPIO as GPIO
import time
import urllib3
http = urllib3.PoolManager()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT,initial = GPIO.LOW)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
baseURL = "https://api.thingspeak.com/update?api_key=HC5BRM3YICTI19D1"
while True:
    line = ser.readline().decode().strip()
    if len(line) is not 0:
        data = line.split(",")
        hum = data[0]
        temp = data[1]
        pir = data[2]
        url = baseURL+"&field1=%f&field2=%f&field3=%d" %(temp,hum,pir)
        if pir == "1":
            pir  = "True"
            GPIO.output(8,1)
            print("Blink")
            time.sleep(1)
            GPIO.output(8,0)
        else :
            pir = "False"
        print ("temp = {}C, humidity = {} ,motion ={}".format(temp,hum,pir))
