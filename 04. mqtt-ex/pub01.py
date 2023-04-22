import paho.mqtt.client as mqtt
from time import sleep
import json

topic = "iot/kim/control"

control = {
    "led" : 1,
    "door" : "open"
}

client = mqtt.Client()
client.connect("localhost")
client.loop_start()

while True:
    sleep(3)
    msg = json.dumps(control)
    print(msg)
    client.publish(topic, msg)
    # client.loop(2)


