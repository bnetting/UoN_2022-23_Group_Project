from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,700,400)
        self.setWindowTitle("QVBox Layout")

        vbox = QVBoxLayout()
        btn1 = QPushButton("btn 1")
        btn2 = QPushButton("btn 1")
        btn3 = QPushButton("btn 1")
        btn4 = QPushButton("btn 1")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())