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
# world.power()

# test rain
# world.rainfall(0)

# Main process of the world
world.notify()

running = True

def runWorld():
    WORLD_STEP_SPEED = 3
    while(True):
        if(running):
            time.sleep(WORLD_STEP_SPEED)
            world.worldStep()
            world.notify()
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post(f'https://anrs.dk/mst/{user}',data=world.exportJSON(),headers=headers)
            requests.post(f'https://anrs.dk/mst/user?id={user}',headers=headers)
            print('World Step')
            print(f'Temp is: {world._temp}')

        pass


sunProcess = threading.Thread(target=runWorld)
sunProcess.daemon = True
sunProcess.start()

while(True):
    state = input(f'Planet {world._name}: ~~ ')
    if state == 'o':
        world.power()
    if state == 'p':
        running = not running
    if state == 'u':
        world.notify()
    if state == 'r0':
        world.rainfall(0)
        world.notify()
    if state == 'r1':
        world.rainfall(1)
        world.notify()
    if state == 'r2':
        world.rainfall(2)
        world.notify()
    if state == 'r3':
        world.rainfall(3)
        world.notify()
    if state == 'r4':
        world.rainfall(4)
        world.notify()
    if state == 'r5':
        world.rainfall(5)
        world.notify()