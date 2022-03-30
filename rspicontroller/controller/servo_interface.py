from abc import abstractmethod


class ServoStrategy():

    @abstractmethod
    def rotationMethod(self, rotationAmount):
        pass

    @abstractmethod
    def cleanUp(self,pin):
        pass
    
    @abstractmethod
    def bareRoationMethod(self,cycleAmount):
        pass

class Servo():

    def __init__(self, servoStragegy: ServoStrategy) -> None:
        self._servoImplementation = servoStragegy

    def servoStrategy(self) -> ServoStrategy:
        return self._servoImplementation

    def rotate(self,rotationAmount) -> None:
        self._servoImplementation.rotationMethod(rotationAmount)

    def bareRotation(self,cycleAmount) -> None:
        self._servoImplementation.bareRoationMethod(cycleAmount)

    def cleanUp(self) -> None:
        self._servoImplementation.cleanUp()