#  pyuic6 -x welcome_page.ui -o ui_welcome_page.py
#  pyrcc5 resources.qrc -o resources_rc.py -- Change PyQt5 to PyQt6 in generated file
#  Ensure welcome.py is the at the top of the stack before compiling.

import time
import os
import sys # sys variables needed to run UI
from main_user_interface import * # Python version of the UI file for welcome page
from PyQt6.QtWidgets import QMainWindow, QApplication, QGraphicsOpacityEffect
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QTimer
import resources_rc



class MainWindow(QMainWindow): #Setup code for welcome page
    def __init__(self, parent=None): 
        QMainWindow.__init__(self) 
        self.ui = Ui_MainWindow() #puts ui_welcome_Page into variable
        self.ui.setupUi(self) #sets up the screen
        self.nextPage = 0        
        self.openWelcome() #Run when the program first starts. Hides the welcome page elements and brings them in with an animation
        
        self.ui.pushButton.clicked.connect(lambda: self.changePage(0,1))
        self.ui.commandLinkButton.clicked.connect(lambda: self.changePage(1,2))
        self.ui.pushButton_5.clicked.connect(lambda: self.changePage(2,1))
        
    def changePage(self,currentPageIndex, newPageIndex):
        if (currentPageIndex == 0):
            self.closeWelcome()
        if (currentPageIndex == 1):
            if (newPageIndex == 2):
                self.nextPage = 2
                self.closeLogin()
        if (currentPageIndex == 2):
            self.closeRegister()
        
    def openWelcome(self): #Setup the welcome page and show animations 

        self.ui.bottom_tab.setMaximumHeight(0)
        
        self.ui.animation1 = QPropertyAnimation(self.ui.bottom_tab, b"maximumHeight")
        self.ui.animation1.setDuration(1500)
        self.ui.animation1.setStartValue(0)
        self.ui.animation1.setEndValue(250)
        self.ui.animation1.setEasingCurve(QEasingCurve.Type.InOutQuart)
                
        self.ui.animation2 = QPropertyAnimation(self.ui.bottom_tab, b"maximumHeight")
        self.ui.animation2.setDuration(1500)
        self.ui.animation2.setStartValue(0)
        self.ui.animation2.setEndValue(250)
        self.ui.animation2.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.effect1 = QGraphicsOpacityEffect()
        self.ui.middle_widget.setGraphicsEffect(self.ui.effect1)
        self.ui.animation3 = QPropertyAnimation(self.ui.effect1, b"opacity")
        self.ui.animation3.setDuration(3500)
        self.ui.animation3.setStartValue(0)
        self.ui.animation3.setEndValue(1)
        self.ui.animation3.setEasingCurve(QEasingCurve.Type.InOutCubic)
        
        self.ui.effect2 = QGraphicsOpacityEffect()
        self.ui.bottom_tab.setGraphicsEffect(self.ui.effect2)
        self.ui.animation4 = QPropertyAnimation(self.ui.effect2, b"opacity")
        self.ui.animation4.setDuration(2500)
        self.ui.animation4.setStartValue(0)
        self.ui.animation4.setEndValue(1)
        self.ui.animation4.setEasingCurve(QEasingCurve.Type.InOutCubic)
        
        self.ui.animation1.start()
        self.ui.animation2.start()
        self.ui.animation3.start()
        self.ui.animation4.start()
        
       
    def closeWelcome(self): #Close the Welcome page and transition to the login page
        
        timer = QTimer(self)
        
        self.ui.animation1 = QPropertyAnimation(self.ui.bottom_tab, b"maximumHeight")
        self.ui.animation1.setDuration(1500)
        self.ui.animation1.setStartValue(250)
        self.ui.animation1.setEndValue(0)
        self.ui.animation1.setEasingCurve(QEasingCurve.Type.InOutQuart)
                
        self.ui.animation2 = QPropertyAnimation(self.ui.bottom_tab, b"maximumHeight")
        self.ui.animation2.setDuration(1500)
        self.ui.animation2.setStartValue(250)
        self.ui.animation2.setEndValue(0)
        self.ui.animation2.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.effect1 = QGraphicsOpacityEffect()
        self.ui.middle_widget.setGraphicsEffect(self.ui.effect1)
        self.ui.animation3 = QPropertyAnimation(self.ui.effect1, b"opacity")
        self.ui.animation3.setDuration(1000)
        self.ui.animation3.setStartValue(1)
        self.ui.animation3.setEndValue(0)
        self.ui.animation3.setEasingCurve(QEasingCurve.Type.InOutCubic)
                
        self.ui.effect2 = QGraphicsOpacityEffect()
        self.ui.bottom_tab.setGraphicsEffect(self.ui.effect2)
        self.ui.animation4 = QPropertyAnimation(self.ui.effect2, b"opacity")
        self.ui.animation4.setDuration(1000)
        self.ui.animation4.setStartValue(1)
        self.ui.animation4.setEndValue(0)
        self.ui.animation4.setEasingCurve(QEasingCurve.Type.InOutCubic)
        
        self.ui.animation1.start()
        self.ui.animation2.start()
        self.ui.animation3.start()
        self.ui.animation4.start()
        
        timer.singleShot(1000, self.openLogin) # Used to create a delay when the closing animation has completed before the new animation begins
        
        
    def openLogin(self): #Opens the login page and animations
        self.ui.stackedWidget.setCurrentIndex(1)
        
        self.ui.frame_3.setMaximumWidth(0)
        self.ui.frame_7.setMaximumWidth(0)
               
        self.ui.animation1 = QPropertyAnimation(self.ui.frame_3, b"maximumWidth")
        self.ui.animation1.setDuration(1500)
        self.ui.animation1.setStartValue(0)
        self.ui.animation1.setEndValue(122)
        self.ui.animation1.setEasingCurve(QEasingCurve.Type.InOutQuart)
                
        self.ui.animation2 = QPropertyAnimation(self.ui.frame_3, b"maximumWidth")
        self.ui.animation2.setDuration(1500)
        self.ui.animation2.setStartValue(0)
        self.ui.animation2.setEndValue(122)
        self.ui.animation2.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.animation3 = QPropertyAnimation(self.ui.frame_7, b"maximumWidth")
        self.ui.animation3.setDuration(1500)
        self.ui.animation3.setStartValue(0)
        self.ui.animation3.setEndValue(1027)
        self.ui.animation3.setEasingCurve(QEasingCurve.Type.InOutQuart)
                
        self.ui.animation4 = QPropertyAnimation(self.ui.frame_7, b"maximumWidth")
        self.ui.animation4.setDuration(1500)
        self.ui.animation4.setStartValue(0)
        self.ui.animation4.setEndValue(1027)
        self.ui.animation4.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.effect1 = QGraphicsOpacityEffect()
        self.ui.frame_3.setGraphicsEffect(self.ui.effect1)
        self.ui.animation5 = QPropertyAnimation(self.ui.effect1, b"opacity")
        self.ui.animation5.setDuration(2500)
        self.ui.animation5.setStartValue(0)
        self.ui.animation5.setEndValue(1)
        self.ui.animation5.setEasingCurve(QEasingCurve.Type.InOutCubic)
        
        self.ui.effect2 = QGraphicsOpacityEffect()
        self.ui.frame_7.setGraphicsEffect(self.ui.effect2)
        self.ui.animation6 = QPropertyAnimation(self.ui.effect2, b"opacity")
        self.ui.animation6.setDuration(2500)
        self.ui.animation6.setStartValue(0)
        self.ui.animation6.setEndValue(1)
        self.ui.animation6.setEasingCurve(QEasingCurve.Type.InOutCubic)
        
        self.ui.animation1.start()
        self.ui.animation2.start()
        self.ui.animation3.start()        
        self.ui.animation4.start()
        self.ui.animation5.start()
        self.ui.animation6.start()
        
    def closeLogin(self): #Opens the login page and animations
        
        timer = QTimer(self)
                   
        self.ui.animation1 = QPropertyAnimation(self.ui.frame_3, b"maximumWidth")
        self.ui.animation1.setDuration(1500)
        self.ui.animation1.setStartValue(122)
        self.ui.animation1.setEndValue(0)
        self.ui.animation1.setEasingCurve(QEasingCurve.Type.InOutQuart)
                
        self.ui.animation2 = QPropertyAnimation(self.ui.frame_3, b"maximumWidth")
        self.ui.animation2.setDuration(1500)
        self.ui.animation2.setStartValue(122)
        self.ui.animation2.setEndValue(0)
        self.ui.animation2.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.animation3 = QPropertyAnimation(self.ui.frame_7, b"maximumWidth")
        self.ui.animation3.setDuration(1500)
        self.ui.animation3.setStartValue(1027)
        self.ui.animation3.setEndValue(0)
        self.ui.animation3.setEasingCurve(QEasingCurve.Type.InOutQuart)
                
        self.ui.animation4 = QPropertyAnimation(self.ui.frame_7, b"maximumWidth")
        self.ui.animation4.setDuration(1500)
        self.ui.animation4.setStartValue(1027)
        self.ui.animation4.setEndValue(0)
        self.ui.animation4.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.effect1 = QGraphicsOpacityEffect()
        self.ui.frame_3.setGraphicsEffect(self.ui.effect1)
        self.ui.animation5 = QPropertyAnimation(self.ui.effect1, b"opacity")
        self.ui.animation5.setDuration(1000)
        self.ui.animation5.setStartValue(1)
        self.ui.animation5.setEndValue(0)
        self.ui.animation5.setEasingCurve(QEasingCurve.Type.InOutCubic)
        
        self.ui.effect2 = QGraphicsOpacityEffect()
        self.ui.frame_7.setGraphicsEffect(self.ui.effect2)
        self.ui.animation6 = QPropertyAnimation(self.ui.effect2, b"opacity")
        self.ui.animation6.setDuration(1000)
        self.ui.animation6.setStartValue(1)
        self.ui.animation6.setEndValue(0)
        self.ui.animation6.setEasingCurve(QEasingCurve.Type.InOutCubic)
        
        self.ui.animation1.start()
        self.ui.animation2.start()
        self.ui.animation3.start()        
        self.ui.animation4.start()        
        self.ui.animation5.start()        
        self.ui.animation6.start()
                
        if(self.nextPage == 2):
            timer.singleShot(1000, self.openRegister) #Going to the register page
        
        
    def openRegister(self):
        self.ui.stackedWidget.setCurrentIndex(2)

        self.ui.frame_19.setMaximumHeight(0)
        self.ui.frame_13.setMaximumHeight(0)

        self.ui.animation1 = QPropertyAnimation(self.ui.frame_19, b"maximumHeight")
        self.ui.animation1.setDuration(1500)
        self.ui.animation1.setStartValue(0)
        self.ui.animation1.setEndValue(247)
        self.ui.animation1.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.animation2 = QPropertyAnimation(self.ui.frame_19, b"maximumHeight")
        self.ui.animation2.setDuration(1500)
        self.ui.animation2.setStartValue(0)
        self.ui.animation2.setEndValue(247)
        self.ui.animation2.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.animation3 = QPropertyAnimation(self.ui.frame_13, b"maximumHeight")
        self.ui.animation3.setDuration(1500)
        self.ui.animation3.setStartValue(0)
        self.ui.animation3.setEndValue(308)
        self.ui.animation3.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.animation4 = QPropertyAnimation(self.ui.frame_13, b"maximumHeight")
        self.ui.animation4.setDuration(1500)
        self.ui.animation4.setStartValue(0)
        self.ui.animation4.setEndValue(308)
        self.ui.animation4.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.effect1 = QGraphicsOpacityEffect()
        self.ui.frame_19.setGraphicsEffect(self.ui.effect1)
        self.ui.animation5 = QPropertyAnimation(self.ui.effect1, b"opacity")
        self.ui.animation5.setDuration(2000)
        self.ui.animation5.setStartValue(0)
        self.ui.animation5.setEndValue(1)
        self.ui.animation5.setEasingCurve(QEasingCurve.Type.InOutCubic)
        
        self.ui.effect2 = QGraphicsOpacityEffect()
        self.ui.frame_13.setGraphicsEffect(self.ui.effect2)
        self.ui.animation6 = QPropertyAnimation(self.ui.effect2, b"opacity")
        self.ui.animation6.setDuration(2000)
        self.ui.animation6.setStartValue(0)
        self.ui.animation6.setEndValue(1)
        self.ui.animation6.setEasingCurve(QEasingCurve.Type.InOutCubic)
                
        self.ui.animation1.start()
        self.ui.animation2.start()
        self.ui.animation3.start()
        self.ui.animation4.start()
        self.ui.animation5.start()
        self.ui.animation6.start()
    
    
    def closeRegister(self):
        
        timer = QTimer(self)
        
        self.ui.animation1 = QPropertyAnimation(self.ui.frame_19, b"maximumHeight")
        self.ui.animation1.setDuration(1500)
        self.ui.animation1.setStartValue(247)
        self.ui.animation1.setEndValue(0)
        self.ui.animation1.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.animation2 = QPropertyAnimation(self.ui.frame_19, b"maximumHeight")
        self.ui.animation2.setDuration(1500)
        self.ui.animation2.setStartValue(247)
        self.ui.animation2.setEndValue(0)
        self.ui.animation2.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.animation3 = QPropertyAnimation(self.ui.frame_13, b"maximumHeight")
        self.ui.animation3.setDuration(1500)
        self.ui.animation3.setStartValue(308)
        self.ui.animation3.setEndValue(0)
        self.ui.animation3.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.animation4 = QPropertyAnimation(self.ui.frame_13, b"maximumHeight")
        self.ui.animation4.setDuration(1500)
        self.ui.animation4.setStartValue(308)
        self.ui.animation4.setEndValue(0)
        self.ui.animation4.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.effect1 = QGraphicsOpacityEffect()
        self.ui.frame_19.setGraphicsEffect(self.ui.effect1)
        self.ui.animation5 = QPropertyAnimation(self.ui.effect1, b"opacity")
        self.ui.animation5.setDuration(1000)
        self.ui.animation5.setStartValue(1)
        self.ui.animation5.setEndValue(0)
        self.ui.animation5.setEasingCurve(QEasingCurve.Type.InOutCubic)
        
        self.ui.effect2 = QGraphicsOpacityEffect()
        self.ui.frame_13.setGraphicsEffect(self.ui.effect2)
        self.ui.animation6 = QPropertyAnimation(self.ui.effect2, b"opacity")
        self.ui.animation6.setDuration(1000)
        self.ui.animation6.setStartValue(1)
        self.ui.animation6.setEndValue(0)
        self.ui.animation6.setEasingCurve(QEasingCurve.Type.InOutCubic)
                
        self.ui.animation1.start()
        self.ui.animation2.start()
        self.ui.animation3.start()
        self.ui.animation4.start()
        self.ui.animation5.start()
        self.ui.animation6.start()
        
        timer.singleShot(1000, self.openLogin)
            
app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())
