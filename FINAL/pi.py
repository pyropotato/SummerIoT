import serial
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT, initial = GPIO.LOW)
HOST = "192.168.43.205"
passwd = "potatomqtt"
username = "potato_mqtt"
client = mqtt.Client()
client.username_pw_set(username,passwd)
client.connect(HOST,1883,20)
client.loop_start()
#client.publish('v2',"test1234",qos = 0, retain = False)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(1)
temp_check = 0
hum_check = 0
while True:
#	time.sleep(1)
	line = ser.readline().decode().strip()
	if len(line) is not 0:
		#print(line[0])
		try:
			if line[0] == '!':
				line = line[1:]
				temp = line.split(",")[0]
				hum = line.split(",")[1]
				if temp != temp_check:
					temp_check = temp
					client.publish('final/room/temp',temp,qos = 0, retain = False)
				if hum != hum_check:
					hum_check = hum
					client.publish('final/room/hum',hum,qos = 0,retain = False)
				#print(line)
			elif line[0] == '@':
				ID = line[1:]
				client.publish('final/rfid',ID,qos = 0, retain = False)
				if ID == "AD3D4C9":
					print("Accepted")
					GPIO.output(3,1)
					time.sleep(1)
					GPIO.output(3,0)
				else:
					print("Rejected")
		except KeyboardInterrupt:
			client.loop_stop()
			client.disconnect()
