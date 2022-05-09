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
    
    
        # if a pin is touched
        if cap[i].value:
            print("Data from cap[i] is: {} ", cap[i])
            
            
            #If it is the first pin during interaction
            #if previous_captured_pin == None:
                #previous_captured_pin = i
                
            #If it is the same pin
            #if previous_captured_pin == i:
            #   break

            # check if gesture is going up
            #if previous_captured_pin > i:
                #print("Sun has risen! Your planet is warming up")
                #sun.increase_sun()
                
            #Check if gesture is going down
            #if previous_captured_pin < i:
                #print("Sun has set! Your planet is cooling down")
                #sun.sunclock('low')
            
            #set latest captured pin to the activated pin
            #previous_captured_pin = i
            
            #Reset counter since there has been activity
            counter = 0
        
        #Increment counter because no acitivity
        if counter > 500:
            #print("Interaction reset - previous pin set to None")
            previous_captured_pin = None
            #Reset counter after reset
            counter = 0
