# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(903, 732)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.WelcomePage = QWidget()
        self.WelcomePage.setObjectName(u"WelcomePage")
        self.verticalLayout_4 = QVBoxLayout(self.WelcomePage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.WelcomePage)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.moveToLoginButton = QPushButton(self.WelcomePage)
        self.moveToLoginButton.setObjectName(u"moveToLoginButton")
        self.moveToLoginButton.setStyleSheet(u"padding: 50;")

        self.horizontalLayout_4.addWidget(self.moveToLoginButton)

        self.moveToRegisterButton = QPushButton(self.WelcomePage)
        self.moveToRegisterButton.setObjectName(u"moveToRegisterButton")
        self.moveToRegisterButton.setStyleSheet(u"padding: 50;")

        self.horizontalLayout_4.addWidget(self.moveToRegisterButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.WelcomePage)
        self.RegisterPage = QWidget()
        self.RegisterPage.setObjectName(u"RegisterPage")
        self.verticalLayout_5 = QVBoxLayout(self.RegisterPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.RegisterPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_5)

        self.registerFrame = QFrame(self.frame)
        self.registerFrame.setObjectName(u"registerFrame")
        self.registerFrame.setFrameShape(QFrame.StyledPanel)
        self.registerFrame.setFrameShadow(QFrame.Raised)
        self.passwordRegisterLineEdit = QLineEdit(self.registerFrame)
        self.passwordRegisterLineEdit.setObjectName(u"passwordRegisterLineEdit")
        self.passwordRegisterLineEdit.setGeometry(QRect(80, 200, 113, 22))
        self.label_2 = QLabel(self.registerFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 110, 58, 16))
        self.usernameRegisterLineEdit = QLineEdit(self.registerFrame)
        self.usernameRegisterLineEdit.setObjectName(u"usernameRegisterLineEdit")
        self.usernameRegisterLineEdit.setGeometry(QRect(80, 140, 113, 22))
        self.label_3 = QLabel(self.registerFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 180, 58, 16))
        self.registerButton = QPushButton(self.registerFrame)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(90, 240, 80, 26))

        self.horizontalLayout.addWidget(self.registerFrame)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.RegisterPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.RegisterPage)
        self.LoginPage = QWidget()
        self.LoginPage.setObjectName(u"LoginPage")
        self.verticalLayout_6 = QVBoxLayout(self.LoginPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_6 = QFrame(self.LoginPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_11)

        self.loginPage = QFrame(self.frame_6)
        self.loginPage.setObjectName(u"loginPage")
        self.loginPage.setFrameShape(QFrame.StyledPanel)
        self.loginPage.setFrameShadow(QFrame.Raised)
        self.usernameLoginLineEdit = QLineEdit(self.loginPage)
        self.usernameLoginLineEdit.setObjectName(u"usernameLoginLineEdit")
        self.usernameLoginLineEdit.setGeometry(QRect(80, 120, 113, 22))
        self.passwordLoginLineEdit = QLineEdit(self.loginPage)
        self.passwordLoginLineEdit.setObjectName(u"passwordLoginLineEdit")
        self.passwordLoginLineEdit.setGeometry(QRect(80, 170, 113, 22))
        self.loginPushButton = QPushButton(self.loginPage)
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setGeometry(QRect(100, 220, 80, 26))
        self.label_6 = QLabel(self.loginPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 100, 58, 16))
        self.label_7 = QLabel(self.loginPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 150, 58, 16))

        self.horizontalLayout_3.addWidget(self.loginPage)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_13)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.frame_10 = QFrame(self.LoginPage)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.LoginPage)
        self.UserHomePage = QWidget()
        self.UserHomePage.setObjectName(u"UserHomePage")
        self.label_5 = QLabel(self.UserHomePage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 240, 211, 101))
        self.stackedWidget.addWidget(self.UserHomePage)
        self.AdminHomePage = QWidget()
        self.AdminHomePage.setObjectName(u"AdminHomePage")
        self.label_4 = QLabel(self.AdminHomePage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 200, 281, 181))
        self.label_4.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.AdminHomePage)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.moveToLoginButton.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.moveToRegisterButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.loginPushButton.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Logged In - user level 2 - User", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"LOGGED IN - User level 1 - Admin", None))
    # retranslateUi

