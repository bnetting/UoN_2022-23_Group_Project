#!!NOTE!! - When rebuilding the 'resources_rc.py' file, you need to go into the file and change the import to 'from PySide6 import QtCore' for icons to properly show

import os
import sys

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
                

    def move(self):
        
        if self.ui.Side_Menu_Num == 0: #Checges the manu from open to docked
            self.ui.animation1 = QPropertyAnimation(self.ui.left_menu_widget, b"maximumWidth")
            self.ui.animation1.setDuration(500)
            self.ui.animation1.setStartValue(40)
            self.ui.animation1.setEndValue(160)
            self.ui.animation1.setEasingCurve(QEasingCurve.InOutQuart)
            self.ui.animation1.start()
            
            self.ui.animation2 = QPropertyAnimation(self.ui.left_menu_widget, b"minimumWidth")
            self.ui.animation2.setDuration(500)
            self.ui.animation2.setStartValue(40)
            self.ui.animation2.setEndValue(160)
            self.ui.animation2.setEasingCurve(QEasingCurve.InOutQuart)
            self.ui.animation2.start()
            
            self.ui.Side_Menu_Num = 1
            
        else: # Changes the menu from docked to open 
            self.ui.animation1 = QPropertyAnimation(self.ui.left_menu_widget, b"maximumWidth")
            self.ui.animation1.setDuration(500)
            self.ui.animation1.setStartValue(160)
            self.ui.animation1.setEndValue(40)
            self.ui.animation1.setEasingCurve(QEasingCurve.InOutQuart)
            self.ui.animation1.start()
            
            self.ui.animation2 = QPropertyAnimation(self.ui.left_menu_widget, b"minimumWidth")
            self.ui.animation2.setDuration(500)
            self.ui.animation2.setStartValue(160)
            self.ui.animation2.setEndValue(40)
            self.ui.animation2.setEasingCurve(QEasingCurve.InOutQuart)
            self.ui.animation2.start()
            
            self.ui.Side_Menu_Num = 0        
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())