from led_controller import led_interface, panel, neopixel_impl
import json

# Opening JSON file
f = open('led_controller/patterns.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
print(data['grassland'])
# Closing file
f.close()

led1 = led_interface.LEDStrip(neopixel_impl.NEOPixel(12,10))

p1 = panel.Panel(led1)

grass = led_interface.LEDPattern('grassland',data['grassland']['panel'])

p1.update(grass)