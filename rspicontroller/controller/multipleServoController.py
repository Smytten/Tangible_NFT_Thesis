from controller import servo_interface 
import time

class MultiController():
    def __init__(self,listOfServos: list) -> None:
        self._servos = listOfServos

    def addServo(self,servo: servo_interface.Servo):
        self._servos.append(servo)

    def addActuationPattern(self):
        pass

    def actuatePattern(self,pattern:list):
        for current in range(len(pattern)):
            self._servos[current].bareRotation(2+(pattern[current]/18))
        time.sleep(0.5)
        for servo in self._servos:
            servo.bareRotation(0)

    def simpleRotate(self, rotationAmount):
        for servo in self._servos:
            servo.bareRotation(2+(rotationAmount/18))
        time.sleep(0.5)
        for servo in self._servos:
            servo.bareRotation(0)
            
    def cleanup(self):
        for servo in self._servos:
            servo.cleanUp()
            time.sleep(0.01)
        print("Goodbye!")
