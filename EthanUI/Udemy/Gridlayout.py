from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGridLayout
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,700,400)
        self.setWindowTitle("GridLayout Layout")

        grid = QGridLayout()
        btn1 = QPushButton("btn 1")
        btn2 = QPushButton("btn 1")
        btn3 = QPushButton("btn 1")
        btn4 = QPushButton("btn 1")

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 1, 0)
        grid.addWidget(btn4, 0, 0)

        self.setLayout(grid)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())