"""
We need to turn the UI files into python files to be imported correctly, use the following code in a terminal in the current directory:

pyuic6 -x mainwindow.ui -o mainwindow.py

'-x ___.ui' is the name of the executable .ui file

'-o ___.py' is what the outrput file will be called

"""

from PyQt6.QtWidgets import QApplication, QMainWindow #If we get an error in the future, check the error to see if it wants QMainWindow, QWidget or QDialog
import sys
from PyQt6 import uic

class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("mainwindow.ui", self)

app = QApplication(sys.argv)

window = UI()
window.show()

sys.exit(app.exec())