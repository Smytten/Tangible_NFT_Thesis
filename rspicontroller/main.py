from controller import servo_interface 
from controller import stubServo
from controller import multipleServoController

command = servo_interface.Servo(stubServo.StubServo())
command1 = servo_interface.Servo(stubServo.StubServo())

mc = multipleServoController.MultiController([command,command1])

mc.simpleRotate(180)
mc.simpleRotate(0)
mc.simpleRotate(180)
mc.simpleRotate(0)