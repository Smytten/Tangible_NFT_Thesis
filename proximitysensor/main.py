# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_cap1188.i2c import CAP1188_I2C

i2c = board.I2C()  # uses board.SCL and board.SDA
cap = CAP1188_I2C(i2c)

# SPI setup
# from digitalio import DigitalInOut, Direction
# from adafruit_cap1188.spi import CAP1188_SPI
# spi = board.SPI()
# cs = DigitalInOut(board.D5)
# cap = CAP1188_SPI(spi, cs)

previous_captured_pin = None
counter = 0

while True:
    for i in range(1, 9):
    
        counter +=1
    
        # if a pin is touched
        if cap[i].value:
            
            #If it is the first pin during interaction
            if previous_captured_pin == None:
                previous_captured_pin = i

            # check if gesture is going up
            if previous_captured_pin < i:
                print("Sun has risen! Your planet is warming up")
                
            #Check if gesture is going down
            if previous_captured_pin > i:
                print("Sun has set! Your planet is cooling down")
            
            #set latest captured pin to the activated pin
            previous_captured_pin = i
            
            #Reset counter since there has been activity
            counter = 0
            
        #If all values are false reset previous captured pin to none
        #if any(cap) == False:
        #Increment counter because no acitivity
        if counter > 2000:
            print("Interaction reset - previous pin set to None")
            previous_captured_pin = None
            #Reset counter after reset
            counter = 0
            
