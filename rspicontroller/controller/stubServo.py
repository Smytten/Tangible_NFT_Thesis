from controller import servo_interface 

class StubServo(servo_interface.ServoStrategy):
    def rotationMethod(self,rotationAmount):
        print(rotationAmount)        

    def bareRoation(self, bareRotation):
        print("bareRoation:" + str(bareRotation))

    def cleanUp(self):
        print("did cleanup")