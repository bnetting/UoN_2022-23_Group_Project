from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget): #Window can now access all attributes and methods from QWidget
    def __init__(self):
        super().__init__() #super() gives access to methods and attributes of the parent class

        self.setGeometry(200,200,700,400) #(x,y,width,height)
        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon('kip.jpg'))
        self.setFixedWidth(700)
        self.setFixedHeight(400)
        self.setStyleSheet('background-color:blue')
        self.setWindowOpacity(0.5)


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())