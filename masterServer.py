import threading
import time
from worldBuilder import world, broker
import json
import requests

try:
    from proximitysensor import rainSensing, main
except:
    print("--| WARNING |-- SENSOR MODULE MISSING")


print("----======++++=====-----")
curUser = input("input world url: ")

r = requests.get('https://anrs.dk/mst/test.json')
j = r.json()

world = world.World()

world.importJSON(j)

# Starting Rain detecting script
try:
    rainProcess = threading.Thread(target=rainSensing.activateSensor,args=(world.rainfall,))
    rainProcess.daemon = True
    rainProcess.start() 
except:
    print("--| WARNING |-- RAIN SENSOR NOT ATTACTED")

# Sun detection
try:
    sunProcess = threading.Thread(target=main.sunDetection,args=(world.setHeatSrc,world.getHeatSrc))
    sunProcess.daemon = True
    rainProcess.start()
except:
    print("--| WARNING |-- SUN SENSOR NOT ATTACTED")

# Create the MQTT observer
realBroker = broker.MQTTBroker()
world.attach(realBroker)


# Main process of the world
while(True):
    time.sleep(10)
    world.worldStep()
    world.notify()
    print(world.exportJSON())
    pass
