import os
import time
import urllib3   #https://urllib3.readthedocs.io/en/latest/
import json
http = urllib3.PoolManager()
x = input("Number of Entries: ")
x = int(x)
try:
    url = "https://api.thingspeak.com/channels/815195/feeds.json?api_key=EBHOFJK7E5BL33C2&results=%i" %(x)
    response = http.request('GET',url)
    data = response.data #byte
    data = data.decode('utf8') #converting byte to string
    data = json.loads(data) #convert to dictionary
    #print (data)
    ch_name = data["channel"]["name"] #channel name
    ch_id = data["channel"]["id"] #channel id
    ch_description = data["channel"]["description"]
    field1_name = data["channel"]["field1"]
    field2_name = data["channel"]["field2"]
    print("")
    print ("Name: " + ch_name)
    print ("ID: " + str(ch_id))
    print ("Description: " + ch_description)
    for x in data["feeds"]:
        entry_id = x["entry_id"]
        time = x["created_at"]
        field1 = x["field1"]
        field2 = x["field2"]
        print('ID = {0}  Time = {1}  {4} = {2}  {5} = {3}' .format(entry_id,time,field1,field2,field1_name,field2_name)) #change name accordingly
    time.sleep(1)
except:
    pass
