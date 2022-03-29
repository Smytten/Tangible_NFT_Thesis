
from controller import servo_interface 
from controller import rspiServo

command = servo_interface.Servo(rspiServo.TowerPro(11))
command1 = servo_interface.Servo(rspiServo.TowerPro(13))

servos = []
servos.append(command)
servos.append(command1)

for servo in servos:
    servo.rotate(0)

for servo in servos:
    servo.rotate(180)

for servo in servos:
    servo.rotate(0)

for servo in servos:
    servo.rotate(180)

for servo in servos:
    servo.cleanUp()