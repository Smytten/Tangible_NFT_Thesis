from led_controller import led_interface
import board
import neopixel

class NEOPixel(led_interface.LEDStrategy):

    def __init__(self,pin,resolution) -> None:
        super().__init__()
        self._pin = pin
        self._resolution = resolution
        self._pixels = neopixel.NeoPixel(board.D12,resolution,auto_write=False)

    def setPattern(self, pattnern: led_interface.LEDPattern):
        for count in range(len(pattnern.getPattern())):
            self._pixels[count] = pattnern.getPattern()[count]

    def active(self):
        self._pixels.show()