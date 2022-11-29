from PyQt6.QtWidgets import (QApplication, QWidget, 
QVBoxLayout, QPushButton, QGridLayout, QHBoxLayout, QLabel)
from PyQt6.QtGui import QIcon, QFont
import sys

# Also includes event handling

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,700,400)
        self.setWindowTitle("GridLayout Layout")

        # grid = QGridLayout()
        # btn1 = QPushButton("btn 1")
        # btn2 = QPushButton("btn 1")
        # btn3 = QPushButton("btn 1")
        # btn4 = QPushButton("btn 1")

        # grid.addWidget(btn1, 0, 0)
        # grid.addWidget(btn2, 0, 1)
        # grid.addWidget(btn3, 1, 0)
        # grid.addWidget(btn4, 0, 0)

        # self.setLayout(grid)

        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton("Change Text")
        btn.clicked.connect(self.clicked_btn)
        self.label = QLabel("Default Text")
        hbox.addWidget(btn)
        hbox.addWidget(self.label)
        self.setLayout(hbox)


    def clicked_btn(self):
        self.label.setText("Another Text")
        self.label.setFont(QFont("Times", 15))
        self.label.setStyleSheet("color: red")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())