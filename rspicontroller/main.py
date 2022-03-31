from servo_controller import servo_interface 
from servo_controller import stubServo
from servo_controller import multipleServoController

command = servo_interface.Servo(stubServo.StubServo())
command1 = servo_interface.Servo(stubServo.StubServo())

mc = multipleServoController.MultiController([command,command1])

mc.simpleRotate(180)
mc.simpleRotate(0)
mc.simpleRotate(180)
mc.simpleRotate(0)

rotationPattern1 = [180,0]
rotationPattern2 = [0,180]

mc.actuatePattern(rotationPattern1)
mc.actuatePattern(rotationPattern2)
mc.actuatePattern(rotationPattern1)
mc.actuatePattern(rotationPattern2)