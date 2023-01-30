#  pyuic6 -x welcome_page.ui -o ui_welcome_page.py
#  pyrcc5 resources.qrc -o resources_rc.py -- Change PyQt5 to PyQt6 in generated file
#  Ensure welcome.py is the at the top of the stack before compiling.

import time
import os
import sys # sys variables needed to run UI
import random
import pandas as pd
from main_user_interface import * # Python version of the UI file for welcome page
import resources_rc
from PyQt6.QtWidgets import QMainWindow, QApplication, QGraphicsOpacityEffect, QSizePolicy
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QTimer, QSize
from PyQt6.QtGui import QPainter
from PyQt6 import QtCharts # pip install PyQt6-Charts
from PyQt6.QtCharts import QChart

# DATA CLEANING AND GRAPHING AREA
#--------------------------------------------
df = pd.read_excel(r'prototypeDevelopment1\threats.xlsx') # May need to do a 'pip install pandas' and 'pip install openpyxl' for this to work.

#--------------------------------------------


class MainWindow(QMainWindow): #Setup code for welcome page
    def __init__(self, parent=None): 
        QMainWindow.__init__(self) 
        self.ui = Ui_MainWindow() #puts ui_welcome_Page into variable
        self.ui.setupUi(self) #sets up the screen
        self.nextPage = 0 
        
        self.openWelcome() #Run when the program first starts. Hides the welcome page elements and brings them in with an animation
        
        self.ui.pushButton.clicked.connect(lambda: self.changePage(0,1)) #Runs if the 'Welcome' button is pushed on the welcome page
        self.ui.commandLinkButton.clicked.connect(lambda: self.changePage(1,2))#Runs if the '-> Register' button is pushed on the login page
        self.ui.pushButton_5.clicked.connect(lambda: self.changePage(2,1))#Runs if the 'Register!' button is pushed on the register page
        self.ui.pushButton_6.clicked.connect(lambda: self.changePage(1,3))#Runs if the 'Login' button is pushed on the login page
        
    # changePage()
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    # The point of this function is to manage when a button that should take the user to a new page is pressed. The function will take 2 inputs.
    # 'currentPageIndex' is the page index of the current page, i.e the welcome page is 0, login is 1, register is 2, etc... . Some pages can only transition to one other page,
    # i.e. you can only go from the Welcome page to the Login page and not back, so in this case the closeWelcome() function also opens the login page for us. In other cases, like the 
    # login page, there are multiple paths, i.e. from login page we can log the user in and take them to their home page, or, take them to the register page. To fix this, we use the 
    # second parameter newPageindex to decide what page we go to next depending on what button is pressed, and the variable nextPage is updated to reflect which page needs to be 
    # loaded up after the current one has been faded out.
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def changePage(self,currentPageIndex, newPageIndex): 
        if (currentPageIndex == 0):
            self.closeWelcome()
        if (currentPageIndex == 1):
            if (newPageIndex == 2):
                self.nextPage = 2
            elif (newPageIndex == 3):
                self.nextPage = 3
            self.closeLogin()
        if (currentPageIndex == 2):
            self.closeRegister()
        
    def openWelcome(self): #Setup the welcome page and show animations 

        self.ui.bottom_tab.setMaximumHeight(0) #Set tab size to 0 before it is displayed to the user on startup (makes them look like they come from off screen)
        
        self.ui.animation1 = QPropertyAnimation(self.ui.bottom_tab, b"maximumHeight")
        self.ui.animation1.setDuration(1500)
        self.ui.animation1.setStartValue(0)
        self.ui.animation1.setEndValue(250)
        self.ui.animation1.setEasingCurve(QEasingCurve.Type.InOutQuart)
                
        self.ui.animation2 = QPropertyAnimation(self.ui.bottom_tab, b"maximumHeight") #Note this code has been repeated from above because it makes these kind of transitions much smoother for some reason,
        self.ui.animation2.setDuration(1500)
        self.ui.animation2.setStartValue(0)
        self.ui.animation2.setEndValue(250)
        self.ui.animation2.setEasingCurve(QEasingCurve.Type.InOutQuart)
        
        self.ui.effect1 = QGraphicsOpacityEffect() #Fades the widgets into view to make their transitions seem smoother
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
        
        timer.singleShot(1000, self.openLogin) # Used to create a delay when the closing animation has completed before the new page is loaded in and the animations begin again.
        
        
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
        elif(self.nextPage == 3):
            timer.singleShot(1000, self.openHome)#Going to the home page
        
        
    def openRegister(self): # Open the register page and animations
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
            
            
    def openHome(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        
        series = QtCharts.QPieSeries()
        
        series.append("Phishing",120)
        series.append("DDoS",60)
        series.append("MitM",25)
        series.append("SQL Injection",70)
        series.append("Password Attack",40)
        
        chart = QtCharts.QChart()
        
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.AnimationOption.SeriesAnimations)
        chart.createDefaultAxes()
        chart.setTitle("Test graph")
        
        self.ui.chartView = QtCharts.QChartView(chart)
        self.ui.chartView.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.ui.chartView.chart().setTheme(QtCharts.QChart.ChartTheme.ChartThemeDark)
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHeightForWidth(self.ui.chartView.sizePolicy().hasHeightForWidth())
        
        self.ui.chartView.setSizePolicy(sizePolicy)
        self.ui.chartView.setMinimumSize(QSize(0,300))
        
        self.ui.widget_25.setContentsMargins(0,0,0,0)
        
        layout = QtWidgets.QHBoxLayout(self.ui.widget_25)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.ui.chartView)
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())
