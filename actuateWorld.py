from worldBuilder import world
import requests

try:
    from rspicontroller import actuate
except:
    print("--| WARNING |-- SERVO MODULE MISSING")

r = requests.get('https://anrs.dk/mst/test.json')
j = r.json()

# Setup World
world = world.World()

world.importJSON(j)


# (¯`·.¸¸.·´¯`·.¸¸.·´¯)
# Acutation of the World
try:
    print(world.getActuationHeights())
    # actuate.actuateAll(world.getActuationHeights())
    # actuate.cleanup()
except:
    print("--| FAILED TO ACTUATE WORLD |--")