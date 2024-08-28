from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow, QPushButton

import Init
import InitGui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mock FreeCAD for Development")
        button = QPushButton("Press Me!")
        self.setFixedSize(QSize(1280, 720))
        self.setCentralWidget(button)
