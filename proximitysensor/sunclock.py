# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import colorsys
import threading


class sunController():
    def __init__(self):

        # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
        # NeoPixels must be connected to D10, D12, D18 or D21 to work.
        self.pixel_pin = board.D10

        # The number of NeoPixels
        self.num_pixels = 13
        
        #Start position of sun
        self.current_position = 0

        # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
        # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
        self.ORDER = neopixel.GRB

        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=0.2, auto_write=False, pixel_order=self.ORDER)
            
        self.SUN_COLOR_OFF = (0,0,0)    
        self.SUN_COLOR_LOW = (255,80,0)
        self.SUN_COLOR_HIGH = (255,115,0)
        
    def init_sun(self):
        for i in range(self.num_pixels-1):    
            self.pixels.fill(self.SUN_COLOR_OFF)
            self.pixels[self.current_position+i] = (self.SUN_COLOR_LOW)
            time.sleep(3)
        
    def update_position(self):
        print("updating position")
        #Turn off all pixels
        self.pixels.fill(self.SUN_COLOR_OFF)
        
        #Turn on next position
        self.current_position += 1
        self.pixels[self.current_position] = (self.SUN_COLOR_LOW)
        self.pixels.show()
        
    def increase_sun(self):
        print("sun increased")
        #Turn off all pixels
        self.pixels.fill(self.SUN_COLOR_OFF)
        
        #Increase sun
        self.pixels[self.current_position] = (self.SUN_COLOR_HIGH)
        self.pixels.show()
        
    def decrease_sun(self):
        print("sun decreased")
        #Turn off all pixels
        self.pixels.fill(self.SUN_COLOR_OFF)
        
        #Increase sun
        self.pixels[self.current_position] = (self.SUN_COLOR_LOW)
        self.pixels.show()
        
obj = sunController()
obj.init_sun() 
        
 #Create a new thread for non-blocking change of position over time
#timer = threading.Timer(10.0, sunController.update_position)
#timer.start()
