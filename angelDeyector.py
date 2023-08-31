from machine import Pin, ADC
from customError import *


class AngelDetecor:
    """ A simple class for taking the wind angel and passing it to the Raspberry Pi Pico maxvoltage must not exceed 3.3V.

    Attributes:

        minAngel: An integer denoting the minimum duty value for the detector.

        maxAngel: An integer denoting the maximum duty value for the detector.

    """

    def __init__(self, pin: int or Pin, minVal: int = 2500, maxVal: int = 7500, scale: float = 20, offset: float = 10.2) -> None:
        """ Creates a new Servo Object.

        args:

            pin (int or machine.Pin or machine.PWM): Either an integer denoting the number of the GPIO pin or an already constructed Pin or PWM object that is connected to the servo.

            minVal (int): Optional, denotes the minimum duty value to be used for this servo.

            maxVal (int): Optional, denotes the maximum duty value to be used for this servo.

            scale (float): Optional, the scale of the potentiometer used

            offset (float): Optional, voltage when potentiometer is at zero degrese

        """
        self.pin = pin
        self.minVal = minVal
        self.maxVal = maxVal
        self.scale = scale
        self.offset = offset
        self.angel: float
        if (minVal < 0) or (minVal > 4095):
            raise InvaildRangeValue(0, 4095)
        if (maxVal < 0) or (maxVal > 4095):
            raise InvaildRangeValue(0, 4095)
        if (pin != 26) or (pin != 27) or (pin != 28):
            raise InvaildPinError
        self.adc = ADC(pin)

    def angelFind(self) -> float:
        """ Finds the postion of the wind Detector

        """

        rawVal: int = self.adc.read_u16()
        self.angel = self.scale * rawVal + self.offset  # converts voltage to angle
        if (self.angel < 0) or (self.angel > 180):
            raise InvaledWindAngleError
        return self.angel

    def zero(self) -> None:
        """ sets current postion to zero degrees
        """
        self.angel = 0
