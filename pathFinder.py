from customError import *
from math import acos, sqrt, pi


class PathFinder:
    """ A class for finding the current location and the direction the boat needs to travel
    Attributes:

        startingLocation: the starting coordinates of the boat .

        endingLocation: the ending coordinates of the boat.
    """

    def __init__(self, startCoords: tuple[float, float], endingCoords: tuple[float, float]) -> None:
        """ Creates a new Servo Object.

        args:

            startLocations (tuple[float, float]): the starting coordinates of the boat

            endingLocation (tuple[float, float]): the ending coordinates of the boat 
        """

        self.startLocation = startCoords
        self.endLocation = endingCoords
        self.vector: tuple[float, float]
        self.angel: float
        self.velocity: float

    def findVector(self) -> tuple[float, float]:
        """ Finds the horzontal and vertacal vectors

        """
        x1: float = self.startLocation[0]
        x2: float = self.endLocation[0]
        y1: float = self.startLocation[1]
        y2: float = self.endLocation[1]
        xVector: float = x1 - x2
        yVector: float = y1 - y2
        self.vector = (xVector, yVector)
        return self.vector

    def findAngel(self) -> float:
        """ Finds the angel it has to travel
        """
        adjacent: float = self.vector[0]
        hypotuse: float = sqrt(self.vector[0]**2 + self.vector[1]**2)
        angel = acos(adjacent / hypotuse)
        self.angel = angel * (180/pi)
        return self.angel

    def calcVelocity(self, time: int, distance: int) -> float:
        """ returns the velocity of the boat
        """
        self.velocity = distance / time
        return self.velocity
