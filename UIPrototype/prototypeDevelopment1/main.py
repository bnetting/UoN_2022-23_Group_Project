#  pyuic6 -x welcome_page.ui -o ui_welcome_page.py
#  pyrcc5 resources.qrc -o resources_rc.py -- Change PyQt5 to PyQt6 in generated file

import os
import sys # sys variables needed to run UI
from ui_welcome_page import Ui_MainWindow as Welcome_Page_UI # Python version of the UI file for welcome page
from ui_login_page import Ui_MainWindow as Login_Page_UI
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import pyqtSignal, pyqtSlot
import resources_rc

class MainWindow(QMainWindow): #Setup code for welcome page
    logged = pyqtSignal() #Logging a button press
    def __init__(self, parent=None): 
        QMainWindow.__init__(self) 
        self.ui = Welcome_Page_UI() #puts ui_welcome_Page into variable
        self.ui.setupUi(self) #sets up the screen
        self.ui.pushButton.clicked.connect(self.auth) #Button for switching page
        
    @pyqtSlot() #Button press code
    def auth(self):
        self.logged.emit()
        self.close()
        
class LoginWindow(QMainWindow): # Setup code for login page
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui = Login_Page_UI()
        self.ui.setupUi(self)
        
        
        
        
app = QApplication(sys.argv)

window = MainWindow()
login = LoginWindow()
window.logged.connect(login.show) #Saying to 
window.show()
sys.exit(app.exec())