from servo import Servo
from machine import Pin
from customError import *
import utime

mainServo = Servo(20)
jibServo = Servo(21)
led = Pin("LED", Pin.OUT)

def servo_Map(x: int, in_min: int, in_max: int, out_min: int, out_max: int) -> int:
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def servo_Angle_Main(angle: int):
    if (angle < 0) or (angle > 180):
        raise AngleNotInRangeError("main")
    mainServo.goto(round(servo_Map(angle,0,180,0,1024)))

def servo_Angle_Jib(angle: int):
    if (angle < 0) or (angle > 180):
        raise AngleNotInRangeError("jib")
    jibServo.goto(round(servo_Map(angle,0,180,0,1024)))

def POST():   #POST tests if the servos are broken
    print("Turn left ...")
    for i in range(0,180,10):
        servo_Angle_Main(i)
        servo_Angle_Jib(i)
        utime.sleep(0.05)
    print("Turn right ...")
    for i in range(180,0,-10):
        servo_Angle_Main(i)
        servo_Angle_Jib(i)
        utime.sleep(0.05)
    main()

def points_Sail_Main(windAngle: float) -> int:
    downWind: int = 0
    broadReach: int = 50
    beamReach: int = 100
    closeHaul: int = 180
    if(windAngle > 45) and (windAngle < 90):
        return closeHaul 
    if(windAngle > 90) and (windAngle < 135):
        return beamReach
    if(windAngle > 135) and (windAngle < 180):
        return broadReach
    if windAngle == 180:
        return downWind
    raise InvaledWindAngleError

def points_Sail_Jib(windAngle: float) -> int:
    downWind: int = 0
    broadReach: int = 25
    beamReach: int = 120
    closeHaul: int = 180
    if(windAngle > 45) and (windAngle < 90):
        return closeHaul 
    if(windAngle > 90) and (windAngle < 135):
        return beamReach
    if(windAngle > 135) and (windAngle < 180):
        return broadReach
    if windAngle == 180:
        return downWind
    raise InvaledWindAngleError


def main(windAngle: float):
    led.high
    while True:
        try:
            servo_Angle_Main(points_Sail_Main(windAngle))
            servo_Angle_Jib(points_Sail_Jib(windAngle))
        except:
            print("start failed")
            POST()
            
POST()

