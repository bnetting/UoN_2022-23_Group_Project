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
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1131, 740)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.welcome_page = QWidget()
        self.welcome_page.setObjectName(u"welcome_page")
        self.verticalLayout_4 = QVBoxLayout(self.welcome_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.welcome_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setPixmap(QPixmap(u":/icons/icons8-menu-32.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.pushButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.welcome_page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.gridLayout_3 = QGridLayout(self.login_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_9 = QFrame(self.login_page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 70))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic"])
        font2.setPointSize(30)
        font2.setBold(True)
        self.label_5.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_5, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_10)


        self.gridLayout_3.addWidget(self.frame_9, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.login_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon = QIcon()
        icon.addFile(u":/icons/icons8-macos-minimize-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-enlarge-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-cancel-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.gridLayout_3.addWidget(self.frame_4, 0, 1, 1, 1, Qt.AlignRight|Qt.AlignTop)

        self.frame_5 = QFrame(self.login_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setToolTipDuration(0)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_6, 0, Qt.AlignBottom)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.commandLinkButton = QCommandLinkButton(self.frame_8)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(True)
        font3.setUnderline(True)
        self.commandLinkButton.setFont(font3)
        self.commandLinkButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.commandLinkButton)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.gridLayout_3.addWidget(self.frame_5, 1, 1, 1, 1, Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.login_page)
        self.register_page = QWidget()
        self.register_page.setObjectName(u"register_page")
        self.horizontalLayout_5 = QHBoxLayout(self.register_page)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
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
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
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
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit_3 = QLineEdit(self.frame_13)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_9.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.frame_13)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_9.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.frame_13)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_9.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.frame_13)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_9.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.frame_13)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_9.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.frame_13)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_9.addWidget(self.lineEdit_8)

        self.pushButton_5 = QPushButton(self.frame_13)
        self.pushButton_5.setObjectName(u"pushButton_5")

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
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
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
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.frame_19)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_19)


        self.horizontalLayout_5.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.register_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"VCTI", None))
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.lineEdit_2.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username: ", None))
        self.lineEdit.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password: ", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"confirm password", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"confirm email", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"company", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Register!", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Register", None))
    # retranslateUi

