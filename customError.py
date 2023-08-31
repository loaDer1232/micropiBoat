class AngleNotInRangeError(Exception):
    """Exception raised for errors in the servo angle.

    Attributes:
        servo -- servo that had the error
    """

    def __init__(self, servo):
        message = f"angel for {servo} servo not in range (0, 180)"
        super().__init__(message)


class InvaledWindAngleError(Exception):
    """Exception raised for errors in the wind angle.

    """

    def __init__(self):
        message = f"wind angle not in range (0, 180)"
        super().__init__(message)


class InvaildRangeValue(Exception):
    """Exception raised for errors in the MinValue passed

        Attributes:
           minVal (int) -- minimum allowable value
           maxVal (int) -- maximum allowable value

    """

    def __init__(self, minVal: int, maxVal: int):
        message = f"MinValue must be in range ({minVal}, {maxVal})"
        super().__init__(message)


class InvaildPinError(Exception):
    """Exception raised for Invald pin 

    """

    def __init__(self):
        message = f"pin is not valid for this use"
        super().__init__(message)
