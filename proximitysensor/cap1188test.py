# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_cap1188.i2c import CAP1188_I2C

i2c = busio.I2C(board.SCL, board.SDA)
cap = CAP1188_I2C(i2c)

#i2c = board.I2C()  # uses board.SCL and board.SDA
#cap = CAP1188_I2C(i2c)

# SPI setup
# from digitalio import DigitalInOut, Direction
# from adafruit_cap1188.spi import CAP1188_SPI
# spi = board.SPI()
# cs = DigitalInOut(board.D5)
# cap = CAP1188_SPI(spi, cs)

while True:
    for i in range(1, 9):
        if cap[i].value:
            print("Pin {} touched!".format(i))

