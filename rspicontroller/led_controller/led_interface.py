from abc import abstractmethod


class LEDPattern():

    def __init__(self, tile_type : str, list : list) -> None:
        self._tileType = tile_type 
        self._tilePattern = list

    def getPattern(self) -> list:
        return self._tilePattern

class LEDStrategy():

    @abstractmethod
    def setPattern(self, pattnern: LEDPattern):
        pass

    def active(self):
        pass


class LEDStrip():

    def __init__(self, servoStragegy: LEDStrategy) -> None:
        self._servoImplementation = servoStragegy

    def LEDStrategy(self) -> LEDStrategy:
        return self._servoImplementation

    def setPattern(self, pattern : LEDPattern):
        self._servoImplementation.setPattern(pattern)

    def active(self):
        self._servoImplementation.active()