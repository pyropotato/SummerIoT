import os
import time
import urllib3   #https://urllib3.readthedocs.io/en/latest/
import Adafruit_DHT
http = urllib3.PoolManager()
while True:
	try:
		hum,temp = Adafruit_DHT.read_retry(11,4)
		#print(hum," humidity")
		#print(temp," temp")
		baseURL = "https://api.thingspeak.com/update?api_key=HC5BRM3YICTI19D1"
		url = baseURL+"&field1=%f,&field2=%f" %(temp,hum)
		#print(url)
		response = http.request('GET',url)
		print (response.data)
		time.sleep(1)
	except:
		pass
