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
        
        
    def controlBrightness(self,r,g,b,amount):
        h,s,v = colorsys.rgb_to_hsv(r, g, b)
        v = v + amount
        new_r, new_g, new_b = colorsys.hsv_to_rgb(h, s, v)
        return new_r, new_g, new_b        

    def sunrise(self):
        print("sunrise")

        while True:
            for i in range(self.num_pixels):
                if i > 3:
                    self.pixels[i-3] = (255, 183, 38)
                if i > 5:
                    self.pixels[i-5] = (0, 0, 0)
                if i < self.num_pixels-1:
                    self.pixels[i+1] = (255, 183, 38)
                    
                #Get turned off color by reducing 100% 
                r,g,b = self.controlBrightness(255,85,0,-1)

                for j in range(0,100,1):
                    #place the values in self.pixels[i] self.pixels[i] = (controlBrightness(...,..,...,..))
                    self.pixels[i] = (self.controlBrightness(r,g,b,0.01))
                    self.pixels.show()
                    time.sleep(0.5)

                """for j in range(135, 30, -1):
                    self.pixels[i] = (255, j, 0)
                    self.pixels.show()
                    time.sleep(0.5)"""

                time.sleep(0.5)

            self.pixels.fill((0, 0, 0))
            self.pixels.show()
            
    def sunset(self):
        print("sunset")


obj = sunController()
obj.sunrise()
