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

thread = threading.Thread(target=rainSensing.activateSensor,args=(world.rainfall,))
try:
    thread.start() 
except (KeyboardInterrupt, SystemExit):
    thread.join(timeout=0)
    sys.exit()
# rainSensing.activateSensor(world.rainfall)
while(True):
    time.sleep(10)
    print(world.exportJSON())
    pass