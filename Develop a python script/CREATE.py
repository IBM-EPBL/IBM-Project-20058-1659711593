import json
import wiotp.sdk.device
import time
myconfig = {
"idebtity": {
"orgId": "hj5fmy",
"typeId": "NodeMCU",
"deviceId": "12345678"
},
"auth": { }
"token": "12345678"
}
client = wiotp.sdk.device.Deviceclient(config=myconfig, logHandlers=None)
client.connect()
while True:
name= "Smartbridge"
#in area location
#latitude=17.4225176
#longitude=78.5458842
#out area location
latitude=17.4219272
longitude=78.5488783
myData={'name': name, 'lat': latitude,'lon': longitude}
client.publishEvent(eventId="status",msgformat="json",
data=mydata, qos=0, onpublish=None)
print("Data published to IBM IOT platform :",myData)
time.sleep(5)
client.disconnect()
