
from controller import servo_interface 
from controller import stubServo

command = servo_interface.Servo(stubServo.StubServo())
command.rotate(0)
command.rotate(180)
command.rotate(0)
command.clearnUp()