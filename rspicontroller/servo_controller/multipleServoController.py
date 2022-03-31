from servo_controller import servo_interface 
import time

class MultiController():

     
    # Constructor of the MultiController Clas. 
    # Takes as input a list of servo to actuate. 
    def __init__(self,listOfServos: list) -> None:
        self._servos = listOfServos


    # Append a servo to the list of controlled servos
    def addServo(self,servo: servo_interface.Servo):
        self._servos.append(servo)

    def addActuationPattern(self):
        pass

    # Actutate a Pattern given as a list i.e. [ 180, 60, 0 ] as degrees
    # The list must be exactly as long as the amount of servos.
    def actuatePattern(self,pattern:list):
        if len(pattern) != len(self._servos):
            raise ValueError("Actutaion Pattern must match amount of Actuators")

        for current in range(len(pattern)):
            self._servos[current].bareRotation(2+(pattern[current]/18))
        time.sleep(0.5)
        for servo in self._servos:
            servo.bareRotation(0)

    # Method Does a simple rotation of all appendet actuators. Takes as
    # input a roation amount in degrees and sets all servos to that amount
    def simpleRotate(self, rotationAmount):
        for servo in self._servos:
            servo.bareRotation(2+(rotationAmount/18))
        time.sleep(0.5)
        for servo in self._servos:
            servo.bareRotation(0)

    # Clean up all the servoes GIO pins
    def cleanup(self):
        for servo in self._servos:
            servo.cleanUp()
            time.sleep(0.01)
        print("Goodbye!")
