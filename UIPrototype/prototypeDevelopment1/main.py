#  pyuic6 -x fileName.ui -o {newName.py}

import sys # sys variables needed to run UI
from ui_welcome_page import * # Python version of the UI file for welcome page
from PyQt6.QtWidgets import QMainWindow, QApplication



class MainWindow(QMainWindow):
    def __init__(self, parent=None): 
        QMainWindow().__init__(self) 
        
        self.ui = Ui_MainWindow() #puts ui_welcome_Page into variable
        self.ui.setupUi(self) #sets up the screen
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())