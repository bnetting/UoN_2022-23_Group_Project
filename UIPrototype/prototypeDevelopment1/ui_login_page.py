# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 470)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Yu Gothic"])
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setToolTipDuration(0)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_5, 0, Qt.AlignBottom)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.commandLinkButton = QCommandLinkButton(self.frame_7)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(True)
        font1.setUnderline(True)
        self.commandLinkButton.setFont(font1)
        self.commandLinkButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.commandLinkButton)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignVCenter)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons/icons8-macos-minimize-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-enlarge-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-cancel-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEdit_2.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username: ", None))
        self.lineEdit.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password: ", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
    # retranslateUi

