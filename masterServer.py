from worldBuilder import world
import json

from proximitysensor import rainSensing


world = world.World()

f = open('worldBuilder/world.json')
jf = json.load(f)
world.importJSON(jf)


rainSensing.activateSensor(world.rainfall)