from controller import servo_interface 
from controller import rspiServo
from controller import multipleServoController

command = servo_interface.Servo(rspiServo.TowerPro(11))
command1 = servo_interface.Servo(rspiServo.TowerPro(13))

mc = multipleServoController.MultiController([command,command1])

rotationPattern1 = [180,0]
rotationPattern2 = [0,180]

mc.actuatePattern(rotationPattern1)
mc.actuatePattern([180,180])
mc.actuatePattern([0,180])
mc.actuatePattern([0,90])

mc.cleanup()