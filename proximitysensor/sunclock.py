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
        self.SUN_STRONG = (64,16,0)
        self.SUN_MILD = (32,8,0)
        self.SUN_WEAK = (20,6,0)
        self.SUN_COLOR_OFF = (0,0,0) 
        
    def init_sun(self, start_position): 
        self.pixels.fill(self.SUN_COLOR_OFF)
        self.pixels.show()
        
        self.current_position = start_position
        self.pixels[self.current_position] = (self.SUN_INTENSE)
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
        #print("updating position")
        self.current_position += 1
            
        #Redraw pixels
        self.redraw_pixels()

        #Create a new thread for non-blocking change of position over time
        timer = threading.Timer(0.08, self.update_position)
        timer.start()
        
    def redraw_pixels(self):
        #Reset pixels
        self.pixels.fill(self.SUN_COLOR_OFF)
        
        #Find modded position for infinite looping around strip
        position = self.current_position % self.num_pixels
        
        #level 1
        if self.sun_level == 1: 
            self.pixels[position] = (self.SUN_INTENSE)
            
        if self.sun_level == 2:
            self.pixels.fill(self.SUN_COLOR_OFF)
            self.pixels[position] = (self.SUN_INTENSE)
            self.pixels[position+1] = (self.SUN_STRONG)
            self.pixels[position-1] = (self.SUN_STRONG)
        
        #level 3
        if self.sun_level == 3:
            self.pixels.fill(self.SUN_COLOR_OFF)
            self.pixels[position] = (self.SUN_INTENSE)
            self.pixels[position+1] = (self.SUN_STRONG)
            self.pixels[position-1] = (self.SUN_STRONG)
            self.pixels[position+2] = (self.SUN_MILD)
            self.pixels[position-2] = (self.SUN_MILD)
        
        #level 4
        if self.sun_level == 4:
            self.pixels.fill(self.SUN_COLOR_OFF)
            self.pixels[position] = (self.SUN_INTENSE)
            self.pixels[position+1] = (self.SUN_STRONG)
            self.pixels[position-1] = (self.SUN_STRONG)
            self.pixels[position+2] = (self.SUN_MILD)
            self.pixels[position-2] = (self.SUN_MILD)
            self.pixels[position+3] = (self.SUN_WEAK)
            self.pixels[position-3] = (self.SUN_WEAK)
        
        self.pixels.show()
        
    def increase_sun(self):
        print("sun increased")
        print("current sun stage is: {}".format(self.sun_level))
        
        if self.sun_level == 4:
            print("Sunlevel already max")
            return
        
        #Update level
        self.sun_level += 1
        print("New sun stage is: {}".format(self.sun_level))
        
        #Redraw pixels
        self.redraw_pixels()
        
    def decrease_sun(self):
        print("sun decreased")
        print("current sun stage is: {}".format(self.sun_level))
        
        if self.sun_level == 1:
            print("Sunlevel already lowest")
            return
        
        #Update level
        self.sun_level -= 1
        print("New sun stage is: {}".format(self.sun_level))
        
        #Redraw pixels
        self.redraw_pixels()
        

        
sun = sunController()
sun.update_position()

while input != 'quit':
    command = input()
    if command == "1":
        sun.increase_sun()
    if command == "2":
        sun.decrease_sun()
    if command == "3":
        sun.test_colors()
        
    command = ''
