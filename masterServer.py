from worldBuilder import world
import json

world = world.World()

f = open('worldBuilder/world.json')
jf = json.load(f)
world.importJSON(jf)