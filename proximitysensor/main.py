# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_cap1188.i2c import CAP1188_I2C
from sunclock import sunController

i2c = board.I2C()  # uses board.SCL and board.SDA
cap = CAP1188_I2C(i2c)
sun = sunController()

previous_captured_pin = None
counter = 0


'''
while input != 'quit':
    command = input()
    if command == "1":
        sun.increase_sun()
    if command == "2":
        sun.decrease_sun()
        
    command = ''
'''

while True:
    for i in range(1, 9):
        
        counter +=1
    
    
        # if a pin is touched. cap[i].value is a boolean expression
        if cap[i].value:

            
            #If it is the first pin during interaction
            #if previous_captured_pin == None:
            #   previous_captured_pin = i
                
            #If it is the same pin
            if previous_captured_pin == i:
                break

            # check if gesture is going up
            if cap[4].value and cap[5].value:
                print("Level 1 sensors have activated")

            # check if gesture is going up
            if cap[3].value and cap[6].value:
                print("Level 2 sensors have activated")
                
            # check if gesture is going up
            if cap[2].value and cap[7].value:
                print("Level 3 sensors have activated")
                
            # check if gesture is going up
            if cap[1].value and cap[8].value:
                print("Level 4 sensors have activated")
                
            #set latest captured pin to the activated pin
            previous_captured_pin = i
            
            
            #Reset counter since there has been activity
            counter = 0
        
        #Increment counter because no acitivity
        if counter > 500:
            #print("Interaction reset - previous pin set to None")
            previous_captured_pin = None
            
            #Reset counter after reset
            counter = 0
