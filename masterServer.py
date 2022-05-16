import threading
import sys
import time
from worldBuilder import world, broker
import requests

try:
    from proximitysensor import rainSensing
except:
    print("--| WARNING |-- RAIN MODULE MISSING")
try:
    from proximitysensor import main
except:
    print("--| WARNING |-- SUN MODULE MISSING")


print("(¯`·.¸¸.·´¯`·.¸¸.·´¯)")
user = sys.argv[1]

r = requests.get(f'https://anrs.dk/mst/{user}')
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
    sunProcess = threading.Thread(target=main.sunDetection,args=(world.setHeatSrc,world.getHeatSrc,world.rainfall))
    sunProcess.daemon = True
    sunProcess.start()
except:
    print("Error in rain module")
    pass


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
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(f'https://anrs.dk/mst/{user}',data=world.exportJSON(),headers=headers)
    print(world.exportJSON())

    pass
