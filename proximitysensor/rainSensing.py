import board
import time
from adafruit_cap1188.i2c import CAP1188_I2C

if __name__ == "__main__":
    import CONST as c
else:
    import proximitysensor.CONST as c

i2c = board.I2C()  # uses board.SCL and board.SDA
cap = CAP1188_I2C(i2c,c.RAINSENSOR_ADDRESS)

def activateSensor(callback):
    activations = []
    prevActive = []
    released = []
    timerArr = []

    curTime = time.time()
    for i in range(6):
        timerArr.append(curTime)
        activations.append(0)
        prevActive.append(False)
        released.append(True)

    while True:
        for i in range(1, 7):
            if cap[i].value == False:
                prevActive[i-1] = False
                activations[i-1] = 0
                released[i-1] = True
            if cap[i].value and timerArr[i-1] < time.time():
                if prevActive[i-1]:
                    activations[i-1] += 1
                    if activations[i-1] == c.ACTIVATION_TIME and released[i-1]:
                        print("Pin {} touched!".format(i))
                        callback(i-1)
                        # TODO impl the server call to make it rain :)
                        timerArr[i-1] = time.time() + c.WAIT_DURATION
                        released[i-1] = False
                else:
                    prevActive[i-1] = True

if __name__ == '__main__':
    activations = []
    prevActive = []
    released = []
    timerArr = []
    
    curTime = time.time()
    for i in range(6):
        timerArr.append(curTime)
        activations.append(0)
        prevActive.append(False)
        released.append(True)
    
    while True:
        for i in range(1, 7):
            if cap[i].value == False:
                prevActive[i-1] = False
                activations[i-1] = 0
                released[i-1] = True
            if cap[i].value and timerArr[i-1] < time.time():
                if prevActive[i-1]:
                    activations[i-1] += 1
                    if activations[i-1] == c.ACTIVATION_TIME and released[i-1]:
                        print("Pin {} touched!".format(i))
                        # TODO impl the server call to make it rain :)
                        timerArr[i-1] = time.time() + c.WAIT_DURATION
                        released[i-1] = False
                else:
                    prevActive[i-1] = True
    