from machine import Pin, PWM

class AngelDetecor:
    """ A simple class for taking the wind angel and passing it to the Raspberry Pi Pico.
 
    Attributes:
 
        minAngel: An integer denoting the minimum duty value for the detector.
 
        maxAngel: An integer denoting the maximum duty value for the detector.
 
    """
    def __init__(self, pin: int or Pin or PWM, minVal=2500, maxVal=7500) -> None:
        """ Creates a new Servo Object.
 
        args:
 
            pin (int or machine.Pin or machine.PWM): Either an integer denoting the number of the GPIO pin or an already constructed Pin or PWM object that is connected to the servo.
 
            minVal (int): Optional, denotes the minimum duty value to be used for this servo.
 
            maxVal (int): Optional, denotes the maximum duty value to be used for this servo.
 
        """
        pass

    