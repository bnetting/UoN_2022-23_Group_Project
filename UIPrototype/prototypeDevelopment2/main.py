from main_ui import * # Python version of the UI file for welcome page
from PyQt6.QtWidgets import QMainWindow, QApplication, QGraphicsOpacityEffect, QSizePolicy
import sys, os
class MainWindow(QMainWindow): #Setup code for welcome page
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow() #puts ui_welcome_Page into variable
        self.ui.setupUi(self) #sets up the screen



        self.ui.pushButton_4.clicked.connect(lambda: util_try_login(self.ui.stackedWidget,self.ui.lineEdit_5.text(), self.ui.lineEdit_6.text()))
        self.ui.pushButton_5.clicked.connect(lambda: util_navigate_login(self.ui.stackedWidget))


app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())