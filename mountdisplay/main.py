# python3.6

import random
import inkyphat as inky_display
inky_display.set_colour("red")
inky_display.set_border(inky_display.WHITE)
from PIL import Image, ImageFont, ImageDraw





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

        img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(inky_display.fonts.PressStart2P, 12)
        nameFont = ImageFont.truetype(inky_display.fonts.PressStart2P, 14)
        name = f'{name}'
        message = f'Temprature: {temp}°'
        hum = f'Water: {33}%'
        w, h = font.getsize(message)
        x = 10
        y = (inky_display.HEIGHT / 2) - (h / 2)


        draw.text((x, y-26), name, inky_display.BLACK, nameFont)
        draw.text((x, y), message, inky_display.BLACK, font)
        draw.text((x, y+14), hum, inky_display.BLACK, font)
        inky_display.set_image(img)
        inky_display.show()
        

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