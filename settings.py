import json


class Settings:
    """ A class for reading settings
    Attributes:
        File (str): the JSON file with the settings in it
    """

    def __init__(self, file: str) -> None:
        """ Creates a new Servo Object.

        args:
            File (str): the JSON file with the settings in it
        """
        self.file = file

    def readSettings(self) -> dict:
        with open(self.file, "r") as mainFile:
            x = mainFile.read()
            return json.loads(x)

    def writeSettings(self, settings: dict) -> None:
        with open(self.file, "w") as mainfile:
            mainfile.write(json.dumps(settings))
