# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'databasewindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_createDB = QPushButton(Form)
        self.pushButton_createDB.setObjectName(u"pushButton_createDB")
        self.pushButton_createDB.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_createDB)

        self.verticalSpacer = QSpacerItem(17, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_connectDB = QPushButton(Form)
        self.pushButton_connectDB.setObjectName(u"pushButton_connectDB")
        self.pushButton_connectDB.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_connectDB)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_result = QLabel(Form)
        self.label_result.setObjectName(u"label_result")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_result.setFont(font1)

        self.verticalLayout.addWidget(self.label_result)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_username = QLineEdit(Form)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setFont(font)

        self.horizontalLayout_3.addWidget(self.lineEdit_username)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_password = QLineEdit(Form)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setFont(font)

        self.horizontalLayout_4.addWidget(self.lineEdit_password)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.pushButton_submitInfo = QPushButton(Form)
        self.pushButton_submitInfo.setObjectName(u"pushButton_submitInfo")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton_submitInfo.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton_submitInfo)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Database Name:", None))
        self.pushButton_createDB.setText(QCoreApplication.translate("Form", u"Create Database", None))
        self.pushButton_connectDB.setText(QCoreApplication.translate("Form", u"Database Connection", None))
        self.label_result.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.pushButton_submitInfo.setText(QCoreApplication.translate("Form", u"Enter", None))
    # retranslateUi

