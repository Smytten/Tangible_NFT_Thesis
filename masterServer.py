import threading
import time
from worldBuilder import world
import json
import requests

from proximitysensor import rainSensing, main


print("----======++++=====-----")
curUser = input("input world url: ")

r = requests.get('https://anrs.dk/mst/test.json')
j = r.json()

world = world.World()

f = open('worldBuilder/world.json')
jf = json.load(f)
world.importJSON(j)

# Starting Rain detecting script
try:
    rainProcess = threading.Thread(target=rainSensing.activateSensor,args=(world.rainfall,))
    rainProcess.daemon = True
    rainProcess.start() 
except:
    print("WARNING-- RAIN SENSOR NOT ATTACTED")

# Sun detection
try:
    sunProcess = threading.Thread(target=main.sunDetection,args=(world.setHeatSrc,world.getHeatSrc))
    sunProcess.daemon = True
    rainProcess.start()
except:
    print("WARNING-- SUN SENSOR NOT ATTACTED")


# Main process of the world
while(True):
    time.sleep(10)
    world.worldStep()
    world.notify()
    print(world.exportJSON())
    pass
