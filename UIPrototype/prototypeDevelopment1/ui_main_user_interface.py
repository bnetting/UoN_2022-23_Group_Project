# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_user_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1131, 740)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.welcome_page = QWidget()
        self.welcome_page.setObjectName(u"welcome_page")
        self.welcome_page.setStyleSheet(u"border: none;\n"
"background-color: #232742;")
        self.verticalLayout_4 = QVBoxLayout(self.welcome_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.welcome_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.middle_widget = QWidget(self.frame)
        self.middle_widget.setObjectName(u"middle_widget")
        self.verticalLayout_3 = QVBoxLayout(self.middle_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.middle_widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setFocusPolicy(Qt.NoFocus)
        self.label.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.middle_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setPixmap(QPixmap(u":/icons/icons8-menu-32.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.middle_widget)


        self.verticalLayout_2.addWidget(self.frame)

        self.bottom_tab = QWidget(self.frame_2)
        self.bottom_tab.setObjectName(u"bottom_tab")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bottom_tab.sizePolicy().hasHeightForWidth())
        self.bottom_tab.setSizePolicy(sizePolicy1)
        self.bottom_tab.setMaximumSize(QSize(16777215, 250))
        self.bottom_tab.setStyleSheet(u"background-color: #8D3CDA;\n"
"border-top-left-radius: 80px 80px;\n"
"border-top-right-radius: 80px 80px;")
        self.verticalLayout_11 = QVBoxLayout(self.bottom_tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton = QPushButton(self.bottom_tab)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"color: white;")

        self.verticalLayout_11.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.bottom_tab)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.welcome_page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.login_page.setAutoFillBackground(False)
        self.login_page.setStyleSheet(u"border: none;\n"
"background-color: #232742;")
        self.gridLayout = QGridLayout(self.login_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_7 = QFrame(self.login_page)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setMidLineWidth(-23)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_7)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_21)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setToolTipDuration(0)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_22)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, -1, -1, -1)
        self.lineEdit_2 = QLineEdit(self.frame_22)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"color: white;\n"
"border-radius: 20px;\n"
"padding: 10px;\n"
"border: 1px solid white;")
        self.lineEdit_2.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_22)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: white;")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_22, 0, Qt.AlignBottom)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_23)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.frame_23)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_23)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: white;\n"
"border-radius: 20px;\n"
"padding: 10px;\n"
"border: 1px solid white;")
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_23, 0, Qt.AlignTop)

        self.frame_24 = QFrame(self.frame_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.commandLinkButton = QCommandLinkButton(self.frame_24)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(True)
        font2.setUnderline(True)
        self.commandLinkButton.setFont(font2)
        self.commandLinkButton.setLayoutDirection(Qt.LeftToRight)
        self.commandLinkButton.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.commandLinkButton)

        self.pushButton_6 = QPushButton(self.frame_24)
        self.pushButton_6.setObjectName(u"pushButton_6")
        font3 = QFont()
        font3.setPointSize(22)
        font3.setBold(True)
        font3.setUnderline(True)
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addWidget(self.frame_24)


        self.horizontalLayout_2.addWidget(self.frame_21)


        self.gridLayout.addWidget(self.frame_7, 3, 1, 1, 1)

        self.frame_20 = QFrame(self.login_page)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_20, 4, 2, 1, 1)

        self.frame_4 = QFrame(self.login_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 3, 0, 1, 1)

        self.frame_5 = QFrame(self.login_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_5, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.frame_8 = QFrame(self.login_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 305))
        self.frame_8.setMaximumSize(QSize(16777215, 100))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_8, 4, 1, 1, 1)

        self.frame_6 = QFrame(self.login_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 500))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_6, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.login_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(50, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setStyleSheet(u"background-color: #8D3CDA;\n"
"border-bottom-right-radius: 20px;\n"
"width: 200px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: white;")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_5.addWidget(self.label_5)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.login_page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_9, 0, 2, 1, 1)

        self.frame_10 = QFrame(self.login_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_10, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.login_page)
        self.register_page = QWidget()
        self.register_page.setObjectName(u"register_page")
        self.register_page.setStyleSheet(u"border: none;\n"
"background-color: #232742;")
        self.horizontalLayout_5 = QHBoxLayout(self.register_page)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.register_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_15)

        self.frame_11 = QFrame(self.register_page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(300, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(150, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.frame_13)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy5)
        self.lineEdit_3.setStyleSheet(u"border: 1px solid white;\n"
"margin-bottom: 5px;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px;\n"
"border-radius: 10px;")

        self.verticalLayout_9.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.frame_13)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"border: 1px solid white;\n"
"margin-bottom: 5px;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px;\n"
"border-radius: 10px;")

        self.verticalLayout_9.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.frame_13)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"border: 1px solid white;\n"
"margin-bottom: 5px;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px;\n"
"border-radius: 10px;")

        self.verticalLayout_9.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.frame_13)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"border: 1px solid white;\n"
"margin-bottom: 5px;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px;\n"
"border-radius: 10px;")

        self.verticalLayout_9.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.frame_13)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"border: 1px solid white;\n"
"margin-bottom: 5px;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px;\n"
"border-radius: 10px;")

        self.verticalLayout_9.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.frame_13)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"border: 1px solid white;\n"
"margin-bottom: 5px;\n"
"color: white;\n"
"text-align: center;\n"
"padding: 10px;\n"
"border-radius: 10px;")

        self.verticalLayout_9.addWidget(self.lineEdit_8)

        self.pushButton_5 = QPushButton(self.frame_13)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #8D3CDA;\n"
"border-radius: 10px;\n"
"padding: 10px;\n"
"color: white;")

        self.verticalLayout_9.addWidget(self.pushButton_5)


        self.verticalLayout_8.addWidget(self.frame_13, 0, Qt.AlignHCenter)

        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_14)


        self.horizontalLayout_5.addWidget(self.frame_11)

        self.frame_16 = QFrame(self.register_page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_16)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color: #8D3CDA;\n"
"border-top-left-radius: 80px 80px;\n"
"margin-left: 75px;\n"
"margin-top: 75px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_19)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: white;\n"
"font-size: 50px;")

        self.horizontalLayout_4.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_19)


        self.horizontalLayout_5.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.register_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_7 = QVBoxLayout(self.home_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_25 = QWidget(self.home_page)
        self.widget_25.setObjectName(u"widget_25")

        self.verticalLayout_7.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.home_page)
        self.widget_26.setObjectName(u"widget_26")

        self.verticalLayout_7.addWidget(self.widget_26)

        self.stackedWidget.addWidget(self.home_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_6.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"VCTI", None))
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.lineEdit_2.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password: ", None))
        self.lineEdit.setPlaceholderText("")
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"confirm password", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"confirm email", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"company", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Register!", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Register", None))
    # retranslateUi

