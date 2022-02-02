from ast import While
from pickle import TRUE
from re import I
import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client1, userdata, message):
    print(message.topic + " = " + str(message.payload.decode("utf-8")))
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
########################################
broker_address="193.49.165.77"

S431H_Temp = "emse/fayol/e4/S431H/sensors/03f5ca58-aa70-47b3-980c-c8f486cac9ee/metrics/TEMP"
S431H_Humd = "emse/fayol/e4/S431H/sensors/03f5ca58-aa70-47b3-980c-c8f486cac9ee/metrics/HMDT"
S431H_Lumi = "emse/fayol/e4/S431H/sensors/03f5ca58-aa70-47b3-980c-c8f486cac9ee/metrics/LUMI"

S423_Temp = "emse/fayol/e4/S423/sensors/8aa60f58-fc6f-49e2-a53a-f5cc96bb9021/metrics/TEMP"
S423_Humd = "emse/fayol/e4/S423/sensors/8aa60f58-fc6f-49e2-a53a-f5cc96bb9021/metrics/HMDT"
S423_Lumi = "emse/fayol/e4/S423/sensors/8aa60f58-fc6f-49e2-a53a-f5cc96bb9021/metrics/LUMI"

S424_Temp = "emse/fayol/e4/S424/sensors/24a89ddc-23c8-4d9f-9f5e-cff4eba32fb5/metrics/TEMP"
S424_Humd = "emse/fayol/e4/S424/sensors/24a89ddc-23c8-4d9f-9f5e-cff4eba32fb5/metrics/HMDT"
S424_Lumi = "emse/fayol/e4/S424/sensors/24a89ddc-23c8-4d9f-9f5e-cff4eba32fb5/metrics/LUMI"

S421_Temp = "emse/fayol/e4/S421/sensors/7b051d3a-8547-463d-9d28-a2d50c5098b4/metrics/TEMP"
S421_Humd = "emse/fayol/e4/S421/sensors/7b051d3a-8547-463d-9d28-a2d50c5098b4/metrics/HMDT"
S421_Lumi = "emse/fayol/e4/S421/sensors/7b051d3a-8547-463d-9d28-a2d50c5098b4/metrics/LUMI"

S422_Temp = "emse/fayol/e4/S422/sensors/88cb0522-478a-456c-b63b-9c402b5e03b2/metrics/TEMP"
S422_Humd = "emse/fayol/e4/S422/sensors/88cb0522-478a-456c-b63b-9c402b5e03b2/metrics/HMDT"
S422_Lumi = "emse/fayol/e4/S422/sensors/88cb0522-478a-456c-b63b-9c402b5e03b2/metrics/LUMI"

S425_Temp = "emse/fayol/e4/S425/sensors/70345659-3f50-49af-98e7-bbc93961df92/metrics/TEMP"
S425_Humd = "emse/fayol/e4/S425/sensors/70345659-3f50-49af-98e7-bbc93961df92/metrics/HMDT"
S425_Lumi = "emse/fayol/e4/S425/sensors/70345659-3f50-49af-98e7-bbc93961df92/metrics/LUMI"

S431F_Temp = "emse/fayol/e4/S431F/sensors/f9538ac8-4fdb-4049-9ff6-ac4855e3bcc5/metrics/TEMP"
S431F_Humd = "emse/fayol/e4/S431F/sensors/f9538ac8-4fdb-4049-9ff6-ac4855e3bcc5/metrics/HMDT"
S431F_Lumi = "emse/fayol/e4/S431F/sensors/f9538ac8-4fdb-4049-9ff6-ac4855e3bcc5/metrics/LUMI"

S405_Temp = "emse/fayol/e4/S405/sensors/6bd134b6-339c-4168-9aeb-ae7d0f236851/metrics/TEMP"
S405_HMDT = "emse/fayol/e4/S405/sensors/6bd134b6-339c-4168-9aeb-ae7d0f236851/metrics/HMDT"
S405_LUMI = "emse/fayol/e4/S405/sensors/6bd134b6-339c-4168-9aeb-ae7d0f236851/metrics/LUMI"

S416_Temp = "emse/fayol/e4/S416/sensors/28bb16da-5d54-4882-9c2b-70c746586185/metrics/TEMP"
S416_Humd = "emse/fayol/e4/S416/sensors/28bb16da-5d54-4882-9c2b-70c746586185/metrics/HMDT"
S416_Lumi = "emse/fayol/e4/S416/sensors/28bb16da-5d54-4882-9c2b-70c746586185/metrics/LUMI"

S432_Temp = "emse/fayol/e4/S432/sensors/140ade6c-4418-4d86-a14e-25b7db5ae83b/metrics/TEMP"
S432_humd = "emse/fayol/e4/S432/sensors/140ade6c-4418-4d86-a14e-25b7db5ae83b/metrics/HMDT"
S432_Lumi ="emse/fayol/e4/S432/sensors/140ade6c-4418-4d86-a14e-25b7db5ae83b/metrics/LUMI"

Hall4Nord_Temp = "emse/fayol/e4/Hall4Nord/sensors/757e0b46-0efe-4f36-bf2c-e8008e49d950/metrics/TEMP"
Hall4Nord_Humd = "emse/fayol/e4/Hall4Nord/sensors/757e0b46-0efe-4f36-bf2c-e8008e49d950/metrics/HMDT"
Hall4Nord_Lumi = "emse/fayol/e4/Hall4Nord/sensors/757e0b46-0efe-4f36-bf2c-e8008e49d950/metrics/LUMI"

roomlist =[S431H_Temp,S431H_Temp,S431H_Lumi,S423_Temp,S423_Humd,S423_Lumi,S424_Temp,S424_Humd,S424_Lumi,S421_Temp,S421_Humd,S421_Lumi,S422_Temp,S422_Humd,S422_Lumi,S425_Temp,S425_Humd,S425_Lumi,S431F_Temp,S431F_Humd,S431F_Lumi,S405_Temp,S405_HMDT,S405_LUMI,S416_Temp,S416_Humd,S416_Lumi,S432_Temp,S432_humd,S432_Lumi,Hall4Nord_Temp,Hall4Nord_Humd,Hall4Nord_Lumi]


print("creating new instance")
client1 = mqtt.Client("P1") #create new instance
client1.on_message=on_message #attach function to callback
print("connecting to broker")
client1.connect(broker_address) #connect to broker
while True:
   for i in roomlist:  
      client1.loop_start() #start the loop
      client1.subscribe(i)
      time.sleep(2) # wait
      client1.loop_stop() #stop the loop
 