from servo_controller import servo_interface 
from servo_controller import rspiServo
from servo_controller import multipleServoController

command = servo_interface.Servo(rspiServo.TowerPro(11))
command1 = servo_interface.Servo(rspiServo.TowerPro(13))

servos = [command, command1]

mc = multipleServoController.MultiController([command,command1])

try:
    while True:
        rotations = input(f'Enter inputs for {len(servos)} servos seperated with space: ') 
        pattern = rotations.split()
        map_object = map(int,pattern)
        pattern = list(map_object)
        mc.actuatePattern(pattern)
finally:
    mc.cleanup()