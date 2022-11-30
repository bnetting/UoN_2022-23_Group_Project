#!!NOTE!! - When rebuilding the 'resources_rc.py' file, you need to go into the file and change the import to 'from PySide6 import QtCore' for icons to properly show

import os
import sys
import csv

from PySide6 import QtCharts, QtWidgets
from PySide6.QtCore import QPropertyAnimation, QEasingCurve

from ui_interface import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.Side_Menu_Num = 0
        
        #Exit App Button
        self.ui.pushButton_7.clicked.connect(lambda: sys.exit())
        
        #Minimise Screen Button
        self.ui.pushButton_9.clicked.connect(lambda: window.showMinimized())
        
        #Maximise Screen Button
        self.ui.pushButton_8.clicked.connect(lambda: window.showMaximized())

        #Dock and un-dock the menu
        self.ui.pushButton_6.clicked.connect(self.move)
        
        #Buttons on the left widget to change the page of the stacked widget
        self.ui.pushButton.clicked.connect(self.changePagePer)
        self.ui.pushButton_5.clicked.connect(self.changePageTemp)
        self.ui.pushButton_2.clicked.connect(self.changePageNest)
        self.ui.pushButton_3.clicked.connect(self.changePageLine)
        self.ui.pushButton_4.clicked.connect(self.changePageBar)
                

    def move(self):
        
        if self.ui.Side_Menu_Num == 0: #Checges the manu from open to docked
            self.ui.animation1 = QPropertyAnimation(self.ui.left_menu_widget, b"maximumWidth")
            self.ui.animation1.setDuration(500)
            self.ui.animation1.setStartValue(0)
            self.ui.animation1.setEndValue(160)
            self.ui.animation1.setEasingCurve(QEasingCurve.InOutQuart)
            self.ui.animation1.start()
            
            self.ui.animation2 = QPropertyAnimation(self.ui.left_menu_widget, b"minimumWidth")
            self.ui.animation2.setDuration(500)
            self.ui.animation2.setStartValue(0)
            self.ui.animation2.setEndValue(160)
            self.ui.animation2.setEasingCurve(QEasingCurve.InOutQuart)
            self.ui.animation2.start()
            
            self.ui.Side_Menu_Num = 1
            
        else: # Changes the menu from docked to open 
            self.ui.animation1 = QPropertyAnimation(self.ui.left_menu_widget, b"maximumWidth")
            self.ui.animation1.setDuration(500)
            self.ui.animation1.setStartValue(160)
            self.ui.animation1.setEndValue(0)
            self.ui.animation1.setEasingCurve(QEasingCurve.InOutQuart)
            self.ui.animation1.start()
            
            self.ui.animation2 = QPropertyAnimation(self.ui.left_menu_widget, b"minimumWidth")
            self.ui.animation2.setDuration(500)
            self.ui.animation2.setStartValue(160)
            self.ui.animation2.setEndValue(0)
            self.ui.animation2.setEasingCurve(QEasingCurve.InOutQuart)
            self.ui.animation2.start()
            
            self.ui.Side_Menu_Num = 0        
        
                
    #Functions to change the page of the stacked widget -------------------------------------------------------------
    
    ### Percentage bar chart tab switching and graph development
    def changePagePer(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        
        yearList = {}
        wealth = {}
        rowCount = 0
        
        with open('billionaires.csv') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            for row in csvReader:
                if rowCount > 0:
                    if not row[2] in yearList:
                        yearList[row[2]] = []
                        yearList[row[2]].append({"name": row[0], "wealth": row[4]})
                    else:
                        yearList[row[2]].append({"name": row[0], "wealth": row[4]})
                rowCount += 1
        
        series = QtCharts.QPercentBarSeries()
        
        nameList=[]
        for x in yearList:
            for z in yearList[x]:
                if not z["name"] in nameList:
                    nameList.append(z["name"])
                    
                if not z["name"] in wealth:
                    wealth[z["name"]] = []
                    wealth[z["name"]].append(float(z["wealth"]))
                    
                else:
                    wealth[z["name"]].append(float(z["wealth"]))
        
        #print(nameList)
        #print(wealth)
        
        for x in nameList:
            setattr(self, "set"+str(x), QtCharts.QBarSet(str(x)))
            series.append(getattr(self, "set"+str(x)))
            
            getattr(self, "set"+str(x)).append(wealth[x])
        
        
        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Top Billionares From 1996 to 2014")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        
        categories = yearList
        axis = QtCharts.QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        
        self.ui.chart_view = QtCharts.QChartView(chart)
        self.ui.chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeLight)
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.chart_view.sizePolicy().hasHeightForWidth())
        self.ui.chart_view.setSizePolicy(sizePolicy)
        
        self.ui.chart_view.setMinimumSize(QSize(0,300))
        
        self.ui.percentage_bar_chart.setContentsMargins(0,0,0,0)
        lay= QtWidgets.QHBoxLayout(self.ui.percentage_bar_chart)
        lay.setContentsMargins(0,0,0,0)
        lay.addWidget(self.ui.chart_view)

        csvFile.close()  
        
        
        
        
        
    def changePageTemp(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        
    def changePageNest(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        
    def changePageLine(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        
    def changePageBar(self):
        self.ui.stackedWidget.setCurrentIndex(4)
     
app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())