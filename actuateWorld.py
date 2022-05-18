from worldBuilder import world
import requests
import sys

try:
    from rspicontroller import actuate
except:
    print("--| WARNING |-- SERVO MODULE MISSING")

# Fetch users world 
user = sys.argv[1]

r = requests.get(f'https://anrs.dk/mst/{user}')
j = r.json()

# Setup World
world = world.World()

world.importJSON(j)

outer = 110

flush = (outer,0,0,0,0,0)
high = (0,outer,outer,outer,outer,outer)

# (¯`·.¸¸.·´¯`·.¸¸.·´¯)
# Acutation of the World
try:
    # print(world.getActuationHeights())
    listOfDegrees = world.getActuationHeights()
    listOfDegrees[0] = outer - listOfDegrees[0]
    actuate.actuateAll(flush)
    actuate.actuateAll(high)
    actuate.actuateAll(flush)
    actuate.actuateAll(listOfDegrees)
    actuate.cleanup()
except:
    print("--| FAILED TO ACTUATE WORLD |--")