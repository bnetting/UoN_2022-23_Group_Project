#!!NOTE!! - When rebuilding the 'resources_rc.py' file, you need to go into the file and change the import to 'from PySide6 import QtCore' for icons to properly show

import os
import sys

from ui_interface import *



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(test)
        
        self.show()
        
def test():
    print("test")        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())