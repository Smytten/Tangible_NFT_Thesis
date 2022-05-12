import threading
from worldBuilder import world
import json

from proximitysensor import rainSensing


world = world.World()

f = open('worldBuilder/world.json')
jf = json.load(f)
world.importJSON(jf)

thread = threading.Thread(target=rainSensing.activateSensor,args=world.rainfall)
# rainSensing.activateSensor(world.rainfall)
while(True):
    pass