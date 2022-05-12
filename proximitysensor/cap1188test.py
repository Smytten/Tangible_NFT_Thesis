# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_cap1188.i2c import CAP1188_I2C

if __name__ == "__main__":
    import CONST as c
else:
    import proximitysensor.CONST as c

i2c = board.I2C()  # uses board.SCL and board.SDA
cap1 = CAP1188_I2C(i2c,c.RAINSENSOR_ADDRESS)
cap2 = CAP1188_I2C(i2c,c.SUNSENSOR_ADDRESS)

# SPI setup
# from digitalio import DigitalInOut, Direction
# from adafruit_cap1188.spi import CAP1188_SPI
# spi = board.SPI()
# cs = DigitalInOut(board.D5)
# cap = CAP1188_SPI(spi, cs)

while True:
    for i in range(1, 9):
        if cap1[i].value:
            print("Pin {} touched!".format(i))
        if cap2[i].value:
            print("Pin {} touched!".format(i))

