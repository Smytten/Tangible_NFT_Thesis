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

    def wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


    def rainbow_cycle(self, wait):
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(pixel_index & 255)
            pixels.show()
            time.sleep(wait)
            
    def sunrise(self):
        print("sunrise")
        
        for i in range(num_pixels):
            setPixelColor(i,255,234,209)
            time.sleep(1)
        
        #while True:
        #    #self.pixels.fill((255, 234, 209))
        #    self.pixels.fill((255, 0, 0))
        #    self.pixels.show()
        #    time.sleep(5)
        #    #self.pixels.fill((255, 141, 9))
        #    self.pixels.fill((0, 255, 0))
        #    self.pixels.show()
        #    time.sleep(5)
        
        
    def sunset(self):
        print("sunset")
        

    def run(self):
        while True:
            # Comment this line out if you have RGBW/GRBW NeoPixels
            self.pixels.fill((255, 0, 0))
            # Uncomment this line if you have RGBW/GRBW NeoPixels
            # pixels.fill((255, 0, 0, 0))
            self.pixels.show()
            time.sleep(1)


            self.rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step

obj = sunController()
obj.sunrise()