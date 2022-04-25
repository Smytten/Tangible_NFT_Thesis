import random
import time

from paho.mqtt import client as mqtt_client
import paho.mqtt.publish as pub


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)



class MQTTBroker():

    def __init__(self):
        print("test")
        self.__clientID = f'python-mqtt-{random.randint(0, 1000)}'
        self.__broker = 'public.mqtthq.com'
        self.__port = 1883 
        self.__client = self.connect_mqtt()
        self.__client.loop_start()


    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        print(self.__clientID)
        print(self.__port)
        client = mqtt_client.Client(self.__clientID)
        #client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.connect(self.__broker, self.__port)
        return client



    def update(self,data):
        for d in data:
            result = self.__client.publish(d.getIdentifyer(),d.getTilesToString(),qos=0, retain = True)
            status = result[0]
            if status == 0:
                print(f"Send `{d.getTilesToString()}` to topic `{d.getIdentifyer()}`")
            else:
                print(f"Failed to send message to topic {d.getIdentifyer()}")
    
    def power(self,data):
        for d in data:
            result = self.__client.publish(d.getIdentifyer(),'o',qos=0, retain = True)
            status = result[0]
            if status == 0:
                print(f"Send `o` to topic `{d.getIdentifyer()}`")
            else:
                print(f"Failed to send message to topic {d.getIdentifyer()}")