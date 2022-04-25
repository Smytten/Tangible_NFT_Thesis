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

        """self.SUN_FRAMES = [(255, 51, 0), (228, 98, 33),
                           (205, 105, 56), (175, 96, 57), (139, 90, 65)]
        self.ACCENT_FRAMES = [(255, 179, 0), (230, 133, 36), (198, 126, 54), (
            203, 157, 111), (213, 198, 156), (225, 218, 198)]"""
            
        self.SUN_COLOR = (255,102,0)

    def sunclock(self):
        print("sunclock begin")

        while True:
            for i in range(self.num_pixels-1):
                time.sleep(0.5)
                self.pixels[i] = self.SUN_COLOR
                self.pixel_pin [i-5] = (0,0,0)
                self.pixels.show()
                
obj = sunController()
sunController().sunclock()