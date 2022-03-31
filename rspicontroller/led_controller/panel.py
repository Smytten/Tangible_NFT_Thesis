from led_controller import led_interface


class Panel():
    def __init__(self, led_strip : led_interface.LEDStrip) -> None:
        self._LEDStrip = led_strip


    def update(self, pattern : led_interface.LEDPattern):
        self._LEDStrip.setPattern(pattern)
        self._LEDStrip.active()
        
        pass