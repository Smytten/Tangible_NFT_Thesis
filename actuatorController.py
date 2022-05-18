from worldBuilder import world
import requests
import sys

try:
    from rspicontroller import actuate
except:
    print("--| WARNING |-- SERVO MODULE MISSING")

outer = 110

flush = (outer,0,0,0,0,0)
high = (0,outer,outer,outer,outer,outer)



# (¯`·.¸¸.·´¯`·.¸¸.·´¯)
# Acutation of the World
try:
    actuate.actuateAll(flush)
    actuate.cleanup()
except:
    print("--| FAILED TO ACTUATE WORLD |--")