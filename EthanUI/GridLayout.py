from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QLineEdit, QVBoxLayout, QHBoxLayout,QMainWindow, QGridLayout
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        screen = app.primaryScreen()
        self.setGeometry(200,200,screen.size().width(),screen.size().height())
        self.setWindowTitle("PythonGuisTutorial")
        
        layout = QGridLayout()

        top = QWidget()
        topLayout = QHBoxLayout()
        top.setLayout(topLayout)
        topBtn1 = QPushButton("Top1")
        topBtn2 = QPushButton("Top1")
        topBtn3 = QPushButton("Top1")
        topLayout.addWidget(topBtn1)
        topLayout.addWidget(topBtn2)
        topLayout.addWidget(topBtn3)

        layout.addWidget(top,0,0)


        self.setLayout(layout)

app = QApplication(sys.argv)
app.setStyleSheet("""
    QPushButton{
        background-color: #5F6273;
        border: 2px solid black;
        color: white;
        padding: 5px;
    }
    
    QPushButton:hover{
        background-color: #767A92;
    }

    MainWindow{
        background-color: #44495D;
    }

    .title{
        margin-bottom: 500px;
    }

""")
window = MainWindow()
window.show()
sys.exit(app.exec())