from abc import abstractmethod


class ServoStrategy():

    @abstractmethod
    def rotationMethod(self, rotationAmount):
        pass

class Servo():

    def __init__(self, servoStragegy: ServoStrategy) -> None:
        
        self._servoImplementation = servoStragegy

    def servoStrategy(self) -> ServoStrategy:
        return self._servoImplementation

    def rotate(self,rotationAmount) -> None:
        self._servoImplementation.rotationMethod(rotationAmount)

class ConcreteServo(ServoStrategy):
    def rotationMethod(self,rotationAmount):
        print(rotationAmount)

if __name__ == "__main__":
    context = Servo(ConcreteServo())
    context.rotate(23)