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
mc.cleanup()