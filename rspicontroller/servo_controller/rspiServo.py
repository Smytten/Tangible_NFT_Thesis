from servo_controller import servo_interface 
import RPi.GPIO as GPIO #Requires that it is run on a RSPI with GPIO
import time

class TowerPro(servo_interface.ServoStrategy):
    
    # Constructor for TowerPro SG90 Servo
    # Takes GIO pin as input and initlize the
    # servo. 
    def __init__(self, pin) -> None:
        super().__init__()
        self._pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin,GPIO.OUT)

        self._servo = GPIO.PWM(pin,50) # pin 11 for servo1, pulse 50Hz
        self._servo.start(0)


    # Simple rotation method that allows rotation in degrees
    def rotationMethod(self,rotationAmount):
        self._servo.ChangeDutyCycle(2+(rotationAmount/18))
        time.sleep(0.5)
        self._servo.ChangeDutyCycle(0)
    
    # Bare-Rotation method that allow direct change to the servo
    def bareRotationMethod(self, cycleAmount):
        self._servo.ChangeDutyCycle(cycleAmount)

    # Clean up method that free the the GIO pins utilized to 
    # control the servo. Should be used when exiting code. 
    def cleanUp(self):
        self._servo.stop()
        GPIO.cleanup(self._pin)
        print("Goodbye!")

