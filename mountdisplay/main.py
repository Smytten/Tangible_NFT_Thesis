# python3.6

import random
import sys
from numpy import average
import inkyphat as i
import inky_fast
inky_display = inky_fast.InkyPHATFast("black")
from PIL import Image, ImageFont, ImageDraw
import time
import requests 

user = sys.argv[1]

#Cleaning 
colours = (i.RED, i.BLACK, i.WHITE)
colour_names= ("red", "black", "white")
i.set_colour('red')
for j, c in enumerate(colours):
    print("- updating with %s" % colour_names[j])
    i.set_border(c)
    for x in range(i.WIDTH):
        for y in range(i.HEIGHT):
            i.putpixel((x, y), c)
    i.show()
    time.sleep(1)

            
        
while True:
    r = requests.get(url=f'https://anrs.dk/mst/{user}')
    data = r.json()
    name = data['name'] 
    temp = data['temp']
    water = 0
    try:
        water = data['totalWaterBody']
    except:
        pass

    inky_display.set_border(inky_display.WHITE)
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(i.fonts.PressStart2P, 12)
    nameFont = ImageFont.truetype(i.fonts.PressStart2P, 14)
    name = f'{name}'
    avgTemp =       f'Avg Temp: {temp}°'
    poleTemp =      f'    Pole: {temp-21}°'
    EquatorTemp =   f' Equator: {temp+11}°'
    #hum =           f'Water:    {water}%'

    w, h = font.getsize(avgTemp)
    x = 10
    y = (inky_display.HEIGHT / 2) - (h / 2)


    draw.text((x, y-36), name, inky_display.BLACK, nameFont)
    draw.text((x, y-12), avgTemp, inky_display.BLACK, font)
    draw.text((x, y+2), poleTemp, inky_display.BLACK, font)
    draw.text((x, y+16), EquatorTemp, inky_display.BLACK, font)
    #draw.text((x, y+28), hum, inky_display.BLACK, font)
    inky_display.set_image(img)
    inky_display.show()

    time.sleep(10)