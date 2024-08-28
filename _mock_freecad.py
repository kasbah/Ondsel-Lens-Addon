import sys

from PySide2.QtWidgets import QApplication

from _mock_environment.main import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
