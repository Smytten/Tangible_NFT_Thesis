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
            
        self.SUN_COLOR = (255,102,0)

    def sunclock(self):
        print("sunclock begin")

        while True:
            for i in range(self.num_pixels):
                self.pixels.fill((0,0,0))
                time.sleep(0.5)
                
                if i>=self.num_pixels-1:
                    i = 0
                    
                self.pixels[i] = self.SUN_COLOR
                self.pixels[i+1] = self.SUN_COLOR
                self.pixels[i+2] = self.SUN_COLOR
                self.pixels.show()

                
obj = sunController()
sunController().sunclock()