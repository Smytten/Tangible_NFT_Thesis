import threading
import time
from worldBuilder import world, broker
import json
import requests

try:
    from proximitysensor import rainSensing
except:
    print("--| WARNING |-- RAIN MODULE MISSING")
try:
    from proximitysensor import main
except:
    print("--| WARNING |-- SUN MODULE MISSING")

try:
    from rspicontroller import actuate
except:
    print("--| WARNING |-- SERVO MODULE MISSING")

print("(¯`·.¸¸.·´¯`·.¸¸.·´¯)")
curUser = input("input world url: ")

r = requests.get('https://anrs.dk/mst/test.json')
j = r.json()

# Setup World
world = world.World()

world.importJSON(j)

# (¯`·.¸¸.·´¯`·.¸¸.·´¯)
# Starting Rain detecting script
try:
    rainProcess = threading.Thread(target=rainSensing.activateSensor,args=(world.rainfall,))
    rainProcess.daemon = True
    rainProcess.start() 
except:
    pass

# (¯`·.¸¸.·´¯`·.¸¸.·´¯)
# Sun detection 
try:
    sunProcess = threading.Thread(target=main.sunDetection,args=(world.setHeatSrc,world.getHeatSrc))
    sunProcess.daemon = True
    rainProcess.start()
except:
    pass

# (¯`·.¸¸.·´¯`·.¸¸.·´¯)
# Acutation of the World
try:
    actuate.actuateAll(world.getActuationHeights())
except:
    print("--| FAILED TO ACTUATE WORLD |--")

# (¯`·.¸¸.·´¯`·.¸¸.·´¯)
# Create the MQTT observer
realBroker = broker.MQTTBroker()
world.attach(realBroker)



# Power the planet
world.power()

# test rain
world.rainfall(0)

# Main process of the world
WORLD_STEP_SPEED = 10
while(True):
    time.sleep(WORLD_STEP_SPEED)
    world.worldStep()
    world.notify()
    print(world.exportJSON())
    pass
