#  pyuic6 -x welcome_page.ui -o ui_welcome_page.py
#  pyrcc5 resources.qrc -o resources_rc.py -- Change PyQt5 to PyQt6 in generated file

import os
import sys # sys variables needed to run UI
from ui_welcome_page import * # Python version of the UI file for welcome page
from PyQt6.QtWidgets import QMainWindow, QApplication
import resources_rc

class MainWindow(QMainWindow): 
    def __init__(self, parent=None): 
        QMainWindow.__init__(self) 
        self.ui = Ui_MainWindow() #puts ui_welcome_Page into variable
        self.ui.setupUi(self) #sets up the screen
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())