from controller import servo_interface 

class StubServo(servo_interface.ServoStrategy):
    def rotationMethod(self,rotationAmount):
        print(rotationAmount)        