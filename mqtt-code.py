import paho.mqtt.client as paho
from paho import mqtt
import time
import json

#--------------Client Configs-----------------
usr = "Akhlf"
password = "Akhlf111"
broker = "192.168.1.2"      
port = 1883
connected_flag = False  # will become True when connected
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv311)
client.username_pw_set(usr, password=password)

#-------------Callback Functions--------------
def on_connect(client, userdata, flags, rc, properties=None):
    global connected_flag
    if rc ==0:
        connected_flag=True
        print("CONNACK received with code %s." % rc)
        client.subscribe("sensors/battery", qos=1)
    else:
        print("field to connect")


def on_subscribe(client, userdata, mid, granted_qos, properties=None):
     print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8")
    try:
        json_data = json.loads(data)
        json_data["timestamp"] = time.ctime()
        json_data["topic"] = msg.topic
        print("JSON message:", json_data)
    except json.JSONDecodeError:
        print("Text message:", data)
    


#-------------Assign Callbacks----------------
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
#-------------Connect to Broker----------------
client.connect(broker, port=port)

#-------------Start Loop-----------------------
client.loop_start()
time.sleep(3)
while connected_flag != True:  # Wait for connection
    print("In wait loop")
    time.sleep(1)
#-------------End Loop-------------------------
client.loop_stop()
client.disconnect()


