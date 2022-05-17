# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import time
from adafruit_cap1188.i2c import CAP1188_I2C
if __name__ == "__main__":
    from sunclock import sunController
    import CONST as c
else:
    from proximitysensor.sunclock import sunController
    import proximitysensor.CONST as c 

i2c = board.I2C()  # uses board.SCL and board.SDA
cap = CAP1188_I2C(i2c,c.SUNSENSOR_ADDRESS)

def sunDetection(callback, getHeatStatus, rainBack):
    sun = sunController()
    sun.update_position()

    activations = []
    prevActive = []
    released = []
    timerArr = []

    curTime = time.time()
    for i in range(2):
        timerArr.append(curTime)
        activations.append(0)
        prevActive.append(False)
        released.append(True)


    previous_captured_pin = None
    counter = 0

    sunStatus = getHeatStatus()

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
        
        if sunStatus != getHeatStatus():
            sun.set_level(getHeatStatus()+1) 
            sunStatus = getHeatStatus()


        for i in range(1, 9):

            counter +=1


            # if a pin is touched. cap[i].value is a boolean expression
            if cap[i].value:
                #print(f'{i} has been touched')



                #If it is the first pin during interaction
                #if previous_captured_pin == None:
                #   previous_captured_pin = i

                #If it is the same pin
                if previous_captured_pin == i:
                    break


                if cap[8].value == False and cap[7].value == False:
                    prevActive[0] = False
                    activations[0] = 0
                    released[0] = True
                if cap[8].value and cap[7].value and timerArr[0] < time.time():
                    if prevActive[0]:
                        activations[0] += 1
                        if activations[0] == c.ACTIVATION_TIME and released[0]:
                            rainBack(1)
                            rainBack(2)
                            rainBack(3)
                            # TODO impl the server call to make it rain :)
                            timerArr[0] = time.time() + c.WAIT_DURATION
                            released[0] = False
                    else:
                        prevActive[0] = True

                if cap[1].value == False and cap[2].value == False:
                    prevActive[1] = False
                    activations[1] = 0
                    released[1] = True
                if cap[1].value and cap[2].value and timerArr[1] < time.time():
                    if prevActive[1]:
                        activations[1] += 1
                        if activations[1] == c.ACTIVATION_TIME and released[1]:
                            rainBack(0)
                            rainBack(4)
                            rainBack(5)
                            # TODO impl the server call to make it rain :)
                            timerArr[1] = time.time() + c.WAIT_DURATION
                            released[1] = False
                    else:
                        prevActive[1] = True


                # if cap[8].value and cap[7].value and cap[6].value:
                #     #print('did this')
                #     rainBack(1)
                #     rainBack(2)
                #     rainBack(3)

                # check if gesture is going up
                if cap[4].value and cap[5].value:
               #     print("Level 1 sensors have activated")
                    callback(0)
                    #sun.set_level(1)

                # check if gesture is going up
                if cap[3].value and cap[6].value:
               #     print("Level 2 sensors have activated")
                    callback(1)
                    #sun.set_level(2)

                # check if gesture is going up
                if cap[2].value and cap[7].value:
               #     print("Level 3 sensors have activated")
                    callback(2)
                    #sun.set_level(3)

                # check if gesture is going up
                if cap[1].value and cap[8].value:
               #     print("Level 4 sensors have activated")
                    callback(3)
                    #sun.set_level(4)

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
