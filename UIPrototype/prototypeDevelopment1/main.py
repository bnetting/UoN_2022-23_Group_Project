#  pyuic6 -x welcome_page.ui -o ui_welcome_page.py
#  pyrcc5 resources.qrc -o resources_rc.py -- Change PyQt5 to PyQt6 in generated file
#  Ensure welcome.py is the at the top of the stack before compiling.

import os
import sys # sys variables needed to run UI
from ui_main_user_interface import * # Python version of the UI file for welcome page
from PySide6.QtWidgets import QMainWindow, QApplication
import resources_rc
class MainWindow(QMainWindow): #Setup code for welcome page
    def __init__(self, parent=None): 
        QMainWindow.__init__(self) 
        self.ui = Ui_MainWindow() #puts ui_welcome_Page into variable
        self.ui.setupUi(self) #sets up the screen
        
        self.ui.pushButton.clicked.connect(lambda: self.changePage(0,1))
        self.ui.commandLinkButton.clicked.connect(lambda: self.changePage(1,2))
        self.ui.pushButton_5.clicked.connect(lambda: self.changePage(2,1))
        
    def changePage(self,currentPageIndex, newPageIndex):
        self.ui.stackedWidget.setCurrentIndex(newPageIndex)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())