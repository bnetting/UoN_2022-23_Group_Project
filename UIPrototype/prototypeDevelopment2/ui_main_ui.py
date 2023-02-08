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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 824)
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
        self.passwordRegisterLineEdit.setEchoMode(QLineEdit.Password)
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
        self.passwordLoginLineEdit.setEchoMode(QLineEdit.Password)
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
        self.horizontalLayout_13 = QHBoxLayout(self.UserHomePage)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.menubar = QFrame(self.UserHomePage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setMinimumSize(QSize(0, 0))
        self.menubar.setMaximumSize(QSize(150, 16777214))
        self.verticalLayout_14 = QVBoxLayout(self.menubar)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.titlebox = QFrame(self.menubar)
        self.titlebox.setObjectName(u"titlebox")
        self.titlebox.setMinimumSize(QSize(0, 150))
        self.titlebox.setMaximumSize(QSize(16777215, 150))
        self.titlebox.setFrameShape(QFrame.StyledPanel)
        self.titlebox.setFrameShadow(QFrame.Raised)
        self.titlelabel = QLabel(self.titlebox)
        self.titlelabel.setObjectName(u"titlelabel")
        self.titlelabel.setGeometry(QRect(0, 0, 151, 151))
        self.titlelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.titlebox)

        self.menuoptions = QFrame(self.menubar)
        self.menuoptions.setObjectName(u"menuoptions")
        self.menuoptions.setFrameShape(QFrame.StyledPanel)
        self.menuoptions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.menuoptions)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.threatstbn = QPushButton(self.menuoptions)
        self.threatstbn.setObjectName(u"threatstbn")

        self.verticalLayout_15.addWidget(self.threatstbn)

        self.countermeasurebtn = QPushButton(self.menuoptions)
        self.countermeasurebtn.setObjectName(u"countermeasurebtn")

        self.verticalLayout_15.addWidget(self.countermeasurebtn)

        self.logoutbtn = QPushButton(self.menuoptions)
        self.logoutbtn.setObjectName(u"logoutbtn")

        self.verticalLayout_15.addWidget(self.logoutbtn)


        self.verticalLayout_14.addWidget(self.menuoptions)


        self.horizontalLayout_13.addWidget(self.menubar)

        self.mainContainer = QFrame(self.UserHomePage)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setMinimumSize(QSize(0, 0))
        self.verticalLayout_16 = QVBoxLayout(self.mainContainer)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.titleBox = QFrame(self.mainContainer)
        self.titleBox.setObjectName(u"titleBox")
        self.titleBox.setFrameShape(QFrame.StyledPanel)
        self.titleBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.titleBox)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Menubtnbox = QFrame(self.titleBox)
        self.Menubtnbox.setObjectName(u"Menubtnbox")
        self.Menubtnbox.setMaximumSize(QSize(100, 16777215))
        self.Menubtnbox.setFrameShape(QFrame.StyledPanel)
        self.Menubtnbox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.Menubtnbox)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Menu = QPushButton(self.Menubtnbox)
        self.Menu.setObjectName(u"Menu")

        self.horizontalLayout_12.addWidget(self.Menu)


        self.horizontalLayout_11.addWidget(self.Menubtnbox)

        self.userBox = QFrame(self.titleBox)
        self.userBox.setObjectName(u"userBox")
        self.userBox.setFrameShape(QFrame.StyledPanel)
        self.userBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.userBox)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.userlabel = QLabel(self.userBox)
        self.userlabel.setObjectName(u"userlabel")

        self.horizontalLayout_14.addWidget(self.userlabel)


        self.horizontalLayout_11.addWidget(self.userBox, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.titleBox)

        self.mainBody = QFrame(self.mainContainer)
        self.mainBody.setObjectName(u"mainBody")
        self.mainBody.setMinimumSize(QSize(0, 700))
        self.mainBody.setMaximumSize(QSize(16777215, 750))
        self.mainBody.setFrameShape(QFrame.StyledPanel)
        self.mainBody.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_8 = QFrame(self.mainBody)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_8)


        self.verticalLayout_16.addWidget(self.mainBody)


        self.horizontalLayout_13.addWidget(self.mainContainer)

        self.stackedWidget.addWidget(self.UserHomePage)
        self.AdminHomePage = QWidget()
        self.AdminHomePage.setObjectName(u"AdminHomePage")
        self.horizontalLayout_2 = QHBoxLayout(self.AdminHomePage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.adminSidePanelFrame = QFrame(self.AdminHomePage)
        self.adminSidePanelFrame.setObjectName(u"adminSidePanelFrame")
        self.adminSidePanelFrame.setMaximumSize(QSize(150, 16777215))
        self.adminSidePanelFrame.setFrameShape(QFrame.StyledPanel)
        self.adminSidePanelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.adminSidePanelFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.adminTitleFrame = QFrame(self.adminSidePanelFrame)
        self.adminTitleFrame.setObjectName(u"adminTitleFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adminTitleFrame.sizePolicy().hasHeightForWidth())
        self.adminTitleFrame.setSizePolicy(sizePolicy)
        self.adminTitleFrame.setMaximumSize(QSize(16777215, 60))
        self.adminTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.adminTitleFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.adminTitleFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.adminTitleFrame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_4.setFont(font)

        self.verticalLayout_7.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.adminTitleFrame)

        self.adminPageSelectionFrame = QFrame(self.adminSidePanelFrame)
        self.adminPageSelectionFrame.setObjectName(u"adminPageSelectionFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.adminPageSelectionFrame.sizePolicy().hasHeightForWidth())
        self.adminPageSelectionFrame.setSizePolicy(sizePolicy2)
        self.adminPageSelectionFrame.setFrameShape(QFrame.StyledPanel)
        self.adminPageSelectionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.adminPageSelectionFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.adminThreatButton = QPushButton(self.adminPageSelectionFrame)
        self.adminThreatButton.setObjectName(u"adminThreatButton")
        font1 = QFont()
        font1.setPointSize(13)
        self.adminThreatButton.setFont(font1)

        self.verticalLayout_8.addWidget(self.adminThreatButton)

        self.adminCountermeasuresButton = QPushButton(self.adminPageSelectionFrame)
        self.adminCountermeasuresButton.setObjectName(u"adminCountermeasuresButton")
        font2 = QFont()
        font2.setPointSize(10)
        self.adminCountermeasuresButton.setFont(font2)

        self.verticalLayout_8.addWidget(self.adminCountermeasuresButton)

        self.pushButton_3 = QPushButton(self.adminPageSelectionFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)

        self.verticalLayout_8.addWidget(self.pushButton_3)


        self.verticalLayout_2.addWidget(self.adminPageSelectionFrame)


        self.horizontalLayout_2.addWidget(self.adminSidePanelFrame)

        self.adminContentFrame = QFrame(self.AdminHomePage)
        self.adminContentFrame.setObjectName(u"adminContentFrame")
        self.adminContentFrame.setFrameShape(QFrame.StyledPanel)
        self.adminContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.adminContentFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.adminHeadBarFrame = QFrame(self.adminContentFrame)
        self.adminHeadBarFrame.setObjectName(u"adminHeadBarFrame")
        self.adminHeadBarFrame.setMaximumSize(QSize(16777215, 60))
        self.adminHeadBarFrame.setFrameShape(QFrame.StyledPanel)
        self.adminHeadBarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.adminHeadBarFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_3 = QFrame(self.adminHeadBarFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(60, 400))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.adminToggleSideMenuButton = QPushButton(self.frame_3)
        self.adminToggleSideMenuButton.setObjectName(u"adminToggleSideMenuButton")

        self.horizontalLayout_6.addWidget(self.adminToggleSideMenuButton)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.frame_7 = QFrame(self.adminHeadBarFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.adminPageLabel = QLabel(self.frame_7)
        self.adminPageLabel.setObjectName(u"adminPageLabel")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setUnderline(True)
        self.adminPageLabel.setFont(font3)

        self.verticalLayout_10.addWidget(self.adminPageLabel, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.frame_7)


        self.verticalLayout_9.addWidget(self.adminHeadBarFrame)

        self.adminMainFrame = QFrame(self.adminContentFrame)
        self.adminMainFrame.setObjectName(u"adminMainFrame")
        self.adminMainFrame.setFrameShape(QFrame.StyledPanel)
        self.adminMainFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.adminMainFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.adminContentStackedWidget = QStackedWidget(self.adminMainFrame)
        self.adminContentStackedWidget.setObjectName(u"adminContentStackedWidget")
        self.adminThreatsPage = QWidget()
        self.adminThreatsPage.setObjectName(u"adminThreatsPage")
        self.verticalLayout_11 = QVBoxLayout(self.adminThreatsPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.adminThreatsFrame1 = QFrame(self.adminThreatsPage)
        self.adminThreatsFrame1.setObjectName(u"adminThreatsFrame1")
        self.adminThreatsFrame1.setFrameShape(QFrame.StyledPanel)
        self.adminThreatsFrame1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.adminThreatsFrame1)

        self.adminThreatsFrame2 = QFrame(self.adminThreatsPage)
        self.adminThreatsFrame2.setObjectName(u"adminThreatsFrame2")
        self.adminThreatsFrame2.setFrameShape(QFrame.StyledPanel)
        self.adminThreatsFrame2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.adminThreatsFrame2)

        self.adminContentStackedWidget.addWidget(self.adminThreatsPage)
        self.adminCountermeasuresPage = QWidget()
        self.adminCountermeasuresPage.setObjectName(u"adminCountermeasuresPage")
        self.adminContentStackedWidget.addWidget(self.adminCountermeasuresPage)

        self.gridLayout.addWidget(self.adminContentStackedWidget, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.adminMainFrame)


        self.horizontalLayout_2.addWidget(self.adminContentFrame)

        self.stackedWidget.addWidget(self.AdminHomePage)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


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
        self.titlelabel.setText(QCoreApplication.translate("MainWindow", u"User View", None))
        self.threatstbn.setText(QCoreApplication.translate("MainWindow", u"Threats", None))
        self.countermeasurebtn.setText(QCoreApplication.translate("MainWindow", u"Countermeasures", None))
        self.logoutbtn.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.Menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.userlabel.setText(QCoreApplication.translate("MainWindow", u"User View", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Admin Page", None))
        self.adminThreatButton.setText(QCoreApplication.translate("MainWindow", u"Threats", None))
        self.adminCountermeasuresButton.setText(QCoreApplication.translate("MainWindow", u"Countermeasures", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"???", None))
        self.adminToggleSideMenuButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.adminPageLabel.setText(QCoreApplication.translate("MainWindow", u"temp text", None))
    # retranslateUi

