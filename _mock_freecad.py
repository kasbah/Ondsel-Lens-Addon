import sys

from PySide2.QtWidgets import QApplication

from _mock_environment.main import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.prep_operations()
window.begin_ondsel_lens()
app.exec_()
