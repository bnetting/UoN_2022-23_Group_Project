#  pyuic6 -x welcome_page.ui -o ui_welcome_page.py
#  pyrcc5 resources.qrc -o resources_rc.py -- Change PyQt5 to PyQt6 in generated file
#  Ensure welcome.py is the at the top of the stack before compiling.
import time
import os
import sys # sys variables needed to run UI
from main_user_interface import * # Python version of the UI file for welcome page
from PyQt6.QtWidgets import QMainWindow, QApplication, QGraphicsOpacityEffect
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QParallelAnimationGroup
import resources_rc
class MainWindow(QMainWindow): #Setup code for welcome page
    def __init__(self, parent=None): 
        QMainWindow.__init__(self) 
        self.ui = Ui_MainWindow() #puts ui_welcome_Page into variable
        self.ui.setupUi(self) #sets up the screen
        
        self.firstSetup() #Run when the program first starts. Hides the welcome page elements and brings them in with an animation
        
        self.ui.pushButton.clicked.connect(lambda: self.changePage(0,1))
        self.ui.commandLinkButton.clicked.connect(lambda: self.changePage(1,2))
        self.ui.pushButton_5.clicked.connect(lambda: self.changePage(2,1))
        
    def changePage(self,currentPageIndex, newPageIndex):
        self.ui.stackedWidget.setCurrentIndex(newPageIndex)
        
    def firstSetup(self):

        self.ui.bottom_tab.setMaximumHeight(0)
        
        self.ui.animation1 = QPropertyAnimation(self.ui.bottom_tab, b"maximumHeight")
        self.ui.animation1.setDuration(1500)
        self.ui.animation1.setStartValue(0)
        self.ui.animation1.setEndValue(250)
        self.ui.animation1.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.ui.animation1.start()
                
        self.ui.animation2 = QPropertyAnimation(self.ui.bottom_tab, b"maximumHeight")
        self.ui.animation2.setDuration(1500)
        self.ui.animation2.setStartValue(0)
        self.ui.animation2.setEndValue(250)
        self.ui.animation2.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.ui.animation2.start()
        
        self.ui.effect1 = QGraphicsOpacityEffect()
        self.ui.middle_widget.setGraphicsEffect(self.ui.effect1)
        self.ui.animation3 = QPropertyAnimation(self.ui.effect1, b"opacity")
        self.ui.animation3.setDuration(3500)
        self.ui.animation3.setStartValue(0)
        self.ui.animation3.setEndValue(1)
        self.ui.animation3.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.ui.animation3.start()
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())
