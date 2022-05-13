import threading
import sys
import time
from worldBuilder import world
import json

from proximitysensor import rainSensing


world = world.World()

f = open('worldBuilder/world.json')
jf = json.load(f)
world.importJSON(jf)

# Starting Rain detecting script
rainProcess = threading.Thread(target=rainSensing.activateSensor,args=(world.rainfall,))
rainProcess.daemon = True
rainProcess.start() 

# Main process of the world
while(True):
    time.sleep(10)
    print(world.exportJSON())
    pass