from customError import *


class PathFinder:
    """ A class for finding the current location and the direction the boat needs to travel
    Attributes:

        startingLocation: the starting coords of the boat .

        endingLocation: the ending coords of the boat.
    """

    def __init__(self, startCoords: tuple[float, float], endingCoords: tuple[float, float]) -> None:
        """ Creates a new Servo Object.

        args:

            startLocations (tuple[float, float]): the starting coords of the boat

            endingLocation (tuple[float, float]): the ending coords of the boat 
        """
        
        self.startLocation = startCoords
        self.endLocation = endingCoords
        self.vector: tuple[float, float]

    def findVector(self)-> tuple[float, float]:
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

    def findAngel(self):
        """ Finds the angel it has to travel
        """
         