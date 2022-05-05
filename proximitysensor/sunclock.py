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
        self.num_pixels = 164
        
        #Start position of sun
        self.current_position = 0
        
        #Start level of the sun between lowest 1 and 4 max
        self.sun_level = 1

        # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
        # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
        self.ORDER = neopixel.GRB

        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=0.2, auto_write=False, pixel_order=self.ORDER)
            
            
        #TODO - Create 4 sun stages       
        self.SUN_INTENSE = (255,64,0)
        self.SUN_STRONG = (127,32,0)
        self.SUN_MILD = (64,16,0)
        self.SUN_WEAK = (32,8,0)
        self.SUN_COLOR_OFF = (0,0,0) 
        
    def init_sun(self, start_position): 
        self.pixels.fill(self.SUN_COLOR_OFF)
        self.current_position = start_position
        self.pixels[self.current_position] = (self.SUN_COLOR_LOW)
        self.pixels.show()
        
    def test_colors(self):
        self.pixels.fill(self.SUN_COLOR_OFF)
        self.pixels.show()
        time.sleep(3)
        
        self.pixels.fill(self.SUN_WEAK)
        self.pixels.show()
        time.sleep(3)
        
        self.pixels.fill(self.SUN_MILD)
        self.pixels.show()
        time.sleep(3)
        
        self.pixels.fill(self.SUN_STRONG)
        self.pixels.show()
        time.sleep(3)
        
        self.pixels.fill(self.SUN_INTENSE)
        self.pixels.show()
        time.sleep(3)
        
        
    def update_position(self):
        print("updating position")
        #Turn off all pixels
        self.pixels.fill(self.SUN_COLOR_OFF)
        
        #Check if reached limit
        if (self.current_position+1 == self.num_pixels):
            self.current_position = 0
        else:
        #Turn on next position
            self.pixels[self.current_position] = (self.SUN_COLOR_LOW)
            #self.current_position += 1
            
        self.pixels.show()
        self.current_position += 1
        
        #Create a new thread for non-blocking change of position over time
        timer = threading.Timer(0.15, self.update_position)
        timer.start()
        
        
        
    def increase_sun(self):
        print("sun increased")
        #Turn off all pixels
        self.pixels.fill(self.SUN_COLOR_OFF)
        
        #TODO - get sun_level
        
        #Quick hardcode level
        #if level 1
        #set new level
        
        #if level 2
        #set new level
        
        #if level 3
        #set new level
        
        #if level 4
        #set new level

        
    def decrease_sun(self):
        print("sun decreased")
        #Turn off all pixels
        self.pixels.fill(self.SUN_COLOR_OFF)
        

        
sunController = sunController()
sunController.test_colors()
