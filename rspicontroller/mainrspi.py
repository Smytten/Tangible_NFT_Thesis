from controller import servo_interface 
from controller import rspiServo
from controller import multipleServoController

command = servo_interface.Servo(rspiServo.TowerPro(11))
command1 = servo_interface.Servo(rspiServo.TowerPro(13))

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

mc.cleanup()