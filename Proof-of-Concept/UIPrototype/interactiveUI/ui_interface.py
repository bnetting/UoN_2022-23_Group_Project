# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceeRnUrg.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 495)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"color: #000;\n"
"font-size 12px;\n"
"border: nine;\n"
"background :none;\n"
"}\n"
"\n"
"/* Changes the background colour of the application*/\n"
"#centralwidget{\n"
"background-color: rgb(230, 236, 242);\n"
"}\n"
"\n"
"/* Changes all pages and the side select menu to a darker colour*/\n"
"#left_menu_widget, #percentage_bar_chart, #nested_donuts, #line_charts, #temperature_bar_chart,#_home_page{\n"
"background-color: rgba(213, 223, 232, 100);\n"
"}\n"
"\n"
"/* Changes sorrounding frame colours*/\n"
"#header_frame, #frame_11, #frame_12,#frame_3{\n"
"background-color: rgb(213, 223, 232);\n"
"}\n"
"\n"
"/* Changes the colour of the selection buttons in the left slide widget*/\n"
"#frame_4 QPushButton{\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgb(213, 223, 232);\n"
"}\n"
"\n"
"/* Changes colour of the menu button*/\n"
"#frame_8 QPushButton{\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"background-color: rgb(192, 201, 212);\n"
"}\n"
"\n"
"/* Changes to colouring of minimise, maximise a"
                        "nd close buttons*/\n"
"#frame_9 QPushButton{\n"
"border-radius: 15px;\n"
"background-color: rgb(192, 201, 212);\n"
"border: 2px solid rgb(172, 181, 192);\n"
"}\n"
"\n"
"\n"
"/* Changes colour of buttons when hovered over */\n"
"#frame_4 QPushButton:hover{\n"
"background-color: rgb(193, 203, 212);\n"
"}\n"
"\n"
"#frame_9 QPushButton:hover{\n"
"background-color:rgb(172, 181, 192);\n"
"}\n"
"\n"
"#frame_8 QPushButton:hover{\n"
"background-color:rgb(172, 181, 192);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_menu_widget = QWidget(self.centralwidget)
        self.left_menu_widget.setObjectName(u"left_menu_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_menu_widget.sizePolicy().hasHeightForWidth())
        self.left_menu_widget.setSizePolicy(sizePolicy)
        self.left_menu_widget.setMaximumSize(QSize(0, 16777215))
        self.left_menu_widget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.left_menu_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.left_menu_widget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/icons/icons8-pie-chart-32.png"))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_7.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.left_menu_widget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons/icons8-bar-chart-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-temperature-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-doughnut-chart-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-line-chart-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.left_menu_widget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.header_frame = QFrame(self.frame_2)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.header_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_6 = QPushButton(self.frame_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-menu-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.header_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setUnderline(True)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_2.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.header_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_9 = QPushButton(self.frame_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(30, 30))
        self.pushButton_9.setMaximumSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-macos-minimize-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.frame_9)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons8-enlarge-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.frame_9)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons8-cancel-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_7)


        self.horizontalLayout_2.addWidget(self.frame_9)


        self.verticalLayout_4.addWidget(self.header_frame)

        self.frame_19 = QFrame(self.frame_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.frame_19)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_7)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.percentage_bar_chart = QWidget()
        self.percentage_bar_chart.setObjectName(u"percentage_bar_chart")
        self.frame_14 = QFrame(self.percentage_bar_chart)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(9, 49, 18, 18))
        sizePolicy2.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy2)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_14)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget.addWidget(self.percentage_bar_chart)
        self.temperature_bar_chart = QWidget()
        self.temperature_bar_chart.setObjectName(u"temperature_bar_chart")
        self.frame_16 = QFrame(self.temperature_bar_chart)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(9, 49, 18, 18))
        sizePolicy2.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy2)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_16)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget.addWidget(self.temperature_bar_chart)
        self.nested_donuts = QWidget()
        self.nested_donuts.setObjectName(u"nested_donuts")
        self.frame_18 = QFrame(self.nested_donuts)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(9, 49, 18, 18))
        sizePolicy2.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy2)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_18)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget.addWidget(self.nested_donuts)
        self.line_charts = QWidget()
        self.line_charts.setObjectName(u"line_charts")
        self.frame_20 = QFrame(self.line_charts)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(9, 49, 18, 18))
        sizePolicy2.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy2)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_20)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget.addWidget(self.line_charts)
        self._home_page = QWidget()
        self._home_page.setObjectName(u"_home_page")
        self.verticalLayout_16 = QVBoxLayout(self._home_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_22 = QFrame(self._home_page)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy2.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy2)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_22)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.verticalLayout_16.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self._home_page)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.size_grip = QFrame(self.frame_12)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setGeometry(QRect(90, 70, 120, 80))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_12)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_10.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"QT CHART", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Percentage Bar Chart", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Temperature Records", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Nested Donuts", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Line Charts", None))
        self.pushButton_6.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.pushButton_9.setText("")
        self.pushButton_8.setText("")
        self.pushButton_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Copyright", None))
    # retranslateUi

