# python3.6

import random

from paho.mqtt import client as mqtt_client
import requests 

broker = 'public.mqtthq.com'
port = 1883
topic = "mworld/6dh2/d"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        message = msg.payload.decode()
        print(message)
        r = requests.get(url=f'https://anrs.dk/mst/{message}')
        data = r.json()
        name = data['name'] 
        temp = data['temp']
         
        

        # DO inky phat stuff


    client.subscribe(topic)
    client.on_message = on_message


def run():
    print("Connecting")
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()