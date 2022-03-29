from controller import servo_interface 
import RPi.GPIO as GPIO #Requires that it is run on a RSPI with GPIO
import time

class TowerPro(servo_interface.ServoStrategy):

    def __init__(self, pin) -> None:
        super().__init__()
        _pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)

        _servo = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz
        _servo.start(0)

    def rotationMethod(self,rotationAmount):

        self._servo.ChangeDutyCycle(2+(rotationAmount/18))
        time.sleep(0.5)
        self._servo.ChangeDutyCycle(0)

    def cleanUp(self):
        
        self._servo.stop()
        GPIO.cleanup()
        print("Goodbye!")

