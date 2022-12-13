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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 300)
        self.label_result = QLabel(Form)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(9, 159, 581, 26))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_result.setFont(font)
        self.pushButton_submitInfo = QPushButton(Form)
        self.pushButton_submitInfo.setObjectName(u"pushButton_submitInfo")
        self.pushButton_submitInfo.setGeometry(QRect(9, 261, 75, 30))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton_submitInfo.setFont(font1)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 9, 271, 29))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        self.label.setFont(font2)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font2)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(9, 44, 307, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_createDB = QPushButton(self.widget1)
        self.pushButton_createDB.setObjectName(u"pushButton_createDB")
        self.pushButton_createDB.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_createDB)

        self.verticalSpacer = QSpacerItem(17, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_connectDB = QPushButton(self.widget1)
        self.pushButton_connectDB.setObjectName(u"pushButton_connectDB")
        self.pushButton_connectDB.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_connectDB)

        self.widget2 = QWidget(Form)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(9, 191, 232, 29))
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_username = QLineEdit(self.widget2)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setFont(font2)

        self.horizontalLayout_3.addWidget(self.lineEdit_username)

        self.widget3 = QWidget(Form)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(9, 226, 227, 29))
        self.horizontalLayout_4 = QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_password = QLineEdit(self.widget3)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setFont(font2)

        self.horizontalLayout_4.addWidget(self.lineEdit_password)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_result.setText("")
        self.pushButton_submitInfo.setText(QCoreApplication.translate("Form", u"Enter", None))
        self.label.setText(QCoreApplication.translate("Form", u"Database Name:", None))
        self.pushButton_createDB.setText(QCoreApplication.translate("Form", u"Create Database", None))
        self.pushButton_connectDB.setText(QCoreApplication.translate("Form", u"Database Connection", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Password:", None))
    # retranslateUi

