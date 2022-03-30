from abc import abstractmethod

# ServoStrategy, abstrac class which respresent servo
# requirements which should be implemented
class ServoStrategy():

    # Do a simple rotation with a rotation amount in 
    # degrees. 
    @abstractmethod
    def rotationMethod(self, rotationAmount):
        pass

    # Cleanup the pin/s used to control the servo
    @abstractmethod
    def cleanUp(self,pin):
        pass
    
    # Perform a bare rotation of utilizing the value
    # the specific servo allows for. 
    @abstractmethod
    def bareRotationMethod(self,cycleAmount):
        pass

class Servo():

    def __init__(self, servoStragegy: ServoStrategy) -> None:
        self._servoImplementation = servoStragegy

    def servoStrategy(self) -> ServoStrategy:
        return self._servoImplementation

    def rotate(self,rotationAmount) -> None:
        self._servoImplementation.rotationMethod(rotationAmount)

    def bareRotation(self,cycleAmount) -> None:
        self._servoImplementation.bareRotationMethod(cycleAmount)

    def cleanUp(self) -> None:
        self._servoImplementation.cleanUp()