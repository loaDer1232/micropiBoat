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
