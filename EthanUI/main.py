from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QLineEdit, QVBoxLayout, QHBoxLayout,QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        screen = app.primaryScreen()
        self.setGeometry(200,200,screen.size().width(),screen.size().height())
        self.setWindowTitle("PythonGuisTutorial")

        layout = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addLayout(row3)

        row1.addWidget(QPushButton("Hello"))
        row2.addWidget(QPushButton("Hello"))
        row2.addWidget(QPushButton("Hello"))
        row3.addWidget(QPushButton("Hello"))


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        
        



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())