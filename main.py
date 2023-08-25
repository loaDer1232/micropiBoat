from servo import Servo
from machine import Pin
import utime

mainServo = Servo(20)
jibServo = Servo(21)
led = Pin("LED", Pin.OUT)

def servo_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def servo_Angle(angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    mainServo.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value
    jibServo.goto(round(servo_Map(angle,0,180,0,1024)))
    

if __name__ == '__main__':
    while True:
        print("Turn left ...")
        for i in range(0,180,10):
            servo_Angle(i)
            utime.sleep(0.05)
        print("Turn right ...")
        for i in range(180,0,-10):
            servo_Angle(i)
            utime.sleep(0.05)