class FreeCADGuiClass:
    def __init__(self):
        self.starting_commands = []
        self.starting_manipulations = []
        self.main_window = None

    # TODO: have mock main call this
    def _set_main_window_ref(self, main_window):
        self.main_window = main_window

    def addCommand(self, key, todo):
        self.starting_commands.append((key, todo))

    def addWorkbenchManipulator(self, manipulation):
        self.starting_manipulations.append(manipulation)

    def getMainWindow(self):
        return self.main_window

FreeCADGui = FreeCADGuiClass()
