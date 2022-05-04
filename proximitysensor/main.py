# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_cap1188.i2c import CAP1188_I2C
from sunclock import sunController

i2c = board.I2C()  # uses board.SCL and board.SDA
cap = CAP1188_I2C(i2c)
sunController = sunController()

previous_captured_pin = None
counter = 0


'''
while input != 'quit':
    command = input()
    if command == "1":
        sunController().sunrise()
    if command == "2":
        sunController().sunset()
        
    command = ''
        '''
        
sunController.update_position()

while True:
    for i in range(1, 9):
        
        counter +=1
    
        # if a pin is touched
        if cap[i].value:
            
            #If it is the first pin during interaction
            if previous_captured_pin == None:
                previous_captured_pin = i

            # check if gesture is going up
            if previous_captured_pin > i:
                print("Sun has risen! Your planet is warming up")
                sunController.increase_sun()
                
                
            #Check if gesture is going down
            if previous_captured_pin < i:
                print("Sun has set! Your planet is cooling down")
                #sun.sunclock('low')
            
            #set latest captured pin to the activated pin
            previous_captured_pin = i
            
            #Reset counter since there has been activity
            counter = 0
            
        #avoid multiple resets if no interaction is happening
        #if previous_captured_pin == None:
        #    break
        
        #Increment counter because no acitivity
        if counter > 500:
            #print("Interaction reset - previous pin set to None")
            previous_captured_pin = None
            #Reset counter after reset
            counter = 0
