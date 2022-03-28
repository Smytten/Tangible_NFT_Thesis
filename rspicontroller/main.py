
from controller import servo_interface 
from controller import stubServo

command = servo_interface.Servo(stubServo.StubServo())
command.rotate(10)
command.rotate(0)