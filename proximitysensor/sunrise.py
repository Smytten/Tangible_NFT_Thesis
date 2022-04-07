# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import colorsys


class sunController():
    def __init__(self):

        # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
        # NeoPixels must be connected to D10, D12, D18 or D21 to work.
        self.pixel_pin = board.D10

        # The number of NeoPixels
        self.num_pixels = 13

        # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
        # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
        self.ORDER = neopixel.GRB

        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=0.2, auto_write=False, pixel_order=self.ORDER)
        
        self.SUN_FRAMES = [(255,85,0), (228,98,33), (205,105,56), (175,96,57), (139,90,65)]
        self.ACCENT_FRAMES = [(255,179,0), (230,133,36), (198,126,54), (203,157,111), (213,198,156), (225,218,198), (255,255,255), (0,0,0)]
        
    def controlBrightness(self,r,g,b,amount):
        #Convert values to float between 0 and 1
        r = r/1000
        g = g/1000
        b = b/1000
        amount = amount/100
        
        
        h,s,v = colorsys.rgb_to_hsv(r, g, b)
        v = v + amount
        new_r, new_g, new_b = colorsys.hsv_to_rgb(h, s, v)
        
        #convert back to real rgb values
        new_r = int(new_r * 1000)
        new_g = int(new_g * 1000)
        new_b = int(new_b * 1000)
        
        
        print("new rgb values are:")
        print(new_r, new_g, new_b)
        return new_r, new_g, new_b        

    def sunrise(self):
        print("sunrise")

        while True:
            for i in range(self.num_pixels):
                
                 #turn on accent color above i
                if i < self.num_pixels-1:
                    for j in reversed(self.ACCENT_FRAMES):
                        self.pixels[i+1] = (j)
                        self.pixels.show()
                        time.sleep(0.2)
                
                #turn on accent color under i through steps
                #change this number for increasing sun size
                if i > 4:
                    for j in reversed(self.ACCENT_FRAMES):
                        self.pixels[i-4] = (j)
                        self.pixels.show()
                        time.sleep(0.1)
                #turn off colors under reverse steps 
                if i > 5:
                    for j in self.ACCENT_FRAMES:
                        self.pixels[i-5] = (j)
                        self.pixels.show()
                        time.sleep(0.1)

                    
                #Control color of i    
                for j in reversed(self.SUN_FRAMES):
                    self.pixels[i] = (j)
                    self.pixels.show()
                    time.sleep(0.1)
                    
                """#Get turned off color by reducing 100% 
                r,g,b = self.controlBrightness(255,85,0,-1)

                for j in range(0,100,1):
                    #place the values in self.pixels[i] self.pixels[i] = (controlBrightness(...,..,...,..))
                    self.pixels[i] = (self.controlBrightness(r,g,b,1))
                    self.pixels.show()
                    time.sleep(0.5)"""

                """for j in range(135, 30, -1):
                    self.pixels[i] = (255, j, 0)
                    self.pixels.show()
                    time.sleep(0.5)"""

                time.sleep(0.2)

            self.pixels.fill((0, 0, 0))
            self.pixels.show()
            
    def sunset(self):
        print("sunset")


obj = sunController()
obj.sunrise()
