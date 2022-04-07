# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


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

        self.KEYFRAMES_RISING = [20, 21, 22, 24, 26, 28, 31, 34, 38, 41, 45, 50, 55, 60, 66, 73, 80, 87, 95,
                                 103, 112, 121, 131, 141, 151, 161, 172, 182, 192, 202, 211, 220, 228, 236,
                                 242, 247, 251, 254, 255]
        
        self.KEYFRAMES_SETTING = [254, 251, 247, 242, 236, 228, 220, 211, 202, 192, 182, 172, 161, 151, 141,
                                  131, 121, 112, 103, 95, 87, 80, 73, 66, 60, 55, 50, 45, 41, 38, 34, 31, 28,
                                  26, 24, 22, 21, 20,
                                  20, 20, 20, 20, 20, 20, 20, 20, 20, 20]

    def sunrise(self):
        print("sunrise")

        while True:
            for i in range(self.num_pixels):
                if i > 3:
                    for frame in self.KEYFRAMES_RISING:
                        self.pixels[i-3] = (frame, 183, 38)
                if i > 5:
                    for frame in self.KEYFRAMES_SETTING:
                        self.pixels[i-5] = (frame, 183, 38)
                if i < self.num_pixels-1:
                    self.pixels[i+1] = (255, 183, 38)

                for j in range(135, 30, -1):
                    self.pixels[i] = (255, j, 0)
                    self.pixels.show()
                    # time.sleep(0.5)

                time.sleep(0.5)

            self.pixels.fill((0, 0, 0))
            self.pixels.show()

    def sunset(self):
        print("sunset")


obj = sunController()
obj.sunrise()
