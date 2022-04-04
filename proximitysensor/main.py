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

previous_captured_pin = 0

while True:
    for i in range(1, 9):
        
        # if a pin is touched
        if cap[i].value:

            # check if previous pin was touched before the current active pin
            if previous_captured_pin < i:
                print("Sun has risen! Your planet is warming up")
                #set latest captured pin to the activated pin

            if previous_captured_pin > i:
                print("Sun has set! Your planet is cooling down")
                #set latest captured pin to the activated pin
            
            previous_captured_pin = i
            

        
