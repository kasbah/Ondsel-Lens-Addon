from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile, QSize
from PySide2.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()
        # self.setFixedSize(QSize(1280, 720))
        # self.ui.setupUi(self)
        # self.setupUi()

    def load_ui(self):
        loader = QUiLoader()
        ui_file = QFile("_mock_environment/MockFreeCADGui.ui")
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self).show()
        ui_file.close()

    def prep_operations(self):
        from CADAccess.MockFreeCAD import FreeCAD
        from CADAccess.MockFreeCADGui import FreeCADGui
        FreeCADGui.set_main_window_ref(self)
        self.add_false_start_panel()

    def begin_ondsel_lens(self):
        import Init
        import InitGui

    def post_operations(self):
        pass

    def add_false_start_panel(self):
        from CADAccess.MockFreeCADGui import FreeCADGui
        FreeCADGui.PySideUic.loadUi("_mock_environment/MockStartPanel.ui")
