from servo_controller import servo_interface 
from servo_controller import rspiServo
from servo_controller import multipleServoController

command0 = servo_interface.Servo(rspiServo.TowerPro(11))
command1 = servo_interface.Servo(rspiServo.TowerPro(13))
command2 = servo_interface.Servo(rspiServo.TowerPro(15))
command3 = servo_interface.Servo(rspiServo.TowerPro(16))
command4 = servo_interface.Servo(rspiServo.TowerPro(18))
command5 = servo_interface.Servo(rspiServo.TowerPro(22))

servos = [command0, command1, command2, command3, command4, command5]

mc = multipleServoController.MultiController(servos)

try:
    while True:
        rotations = input(f'Enter inputs for {len(servos)} servos seperated with space: ') 
        pattern = rotations.split()
        map_object = map(int,pattern)
        pattern = list(map_object)
        if len(pattern) == 1:
            for x in range(len(servos)-1):
                pattern.append(pattern[0])
            mc.actuatePattern(pattern)
        else:
            mc.actuatePattern(pattern)
finally:
    mc.cleanup()