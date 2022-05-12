import board
import time
from adafruit_cap1188.i2c import CAP1188_I2C

if __name__ == "__main__":
    import CONST as c
else:
    import proximitysensor.CONST as c

i2c = board.I2C()  # uses board.SCL and board.SDA
cap = CAP1188_I2C(i2c,c.RAINSENSOR_ADDRESS)

# SPI setup
# from digitalio import DigitalInOut, Direction
# from adafruit_cap1188.spi import CAP1188_SPI
# spi = board.SPI()
# cs = DigitalInOut(board.D5)
# cap = CAP1188_SPI(spi, cs)

activations = []
prevActive = []

timerArr = []
curTime = time.time()
for i in range(6):
    timerArr.append(curTime)
    activations.append(0)
    prevActive.append(False)

while True:
    for i in range(1, 7):
        if cap[i].value and timerArr[i-1] < time.time():
            if prevActive[i-1]:
                activations[i-1] += 1
                if activations[i-1] == 200:
                    print("Pin {} touched!".format(i))
                    timerArr[i-1] = time.time() + 5

            else:
                prevActive[i-1] = True


        else:
            prevActive[i-1] = False
            activations[i-1] = 0

