from os.path import expanduser

from CADAccess.MockConsole import MockConsole
from CADAccess.MockParameters import MockParameters

class FreeCADClass:
    Console = MockConsole()

    def __init__(self):
        self.parameters = MockParameters()

    def ParamGet(self, name=None, default=None):
        if name is None:
            return self.parameters
        return self.parameters._Get(name, default)

    @staticmethod
    def getUserCachePath():
        return str(expanduser("~/.cache/Ondsel/Cache"))

    @staticmethod
    def getUserConfigDir():
        return str(expanduser("~/.config/Ondsel"))

FreeCAD = FreeCADClass()
