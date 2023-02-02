from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import sys
from databasewindowUserPass import Ui_Form as ui
import mysql.connector as mc # Custom import


class AppWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)        
        
    #Adding the buttons connectivity. Note they MUST GO BELOW 'self.setupUi(self)'
        self.pushButton_createDB.clicked.connect(self.createDatabase)
        self.pushButton_connectDB.clicked.connect(self.connectDatabase)
        self.pushButton_submitInfo.clicked.connect(self.insertData)

        self.show()
        
        
   #All code below is added by Ben
   #---------------------------------------
    def createDatabase(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=""
            ) 
            
            cursor = mydb.cursor()
            dbname = self.lineEdit.text()
            
            cursor.execute("CREATE DATABASE {}".format(dbname))
            self.label_result.setText("Database {} created".format(dbname))
            
        except mc.Error as e:
            self.label_result.setText("Database creation fail")
       
    def connectDatabase(self):
        
        dbname = self.lineEdit.text()
        
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database=dbname
            )
            
            self.label_result.setText("There is a connection")
            
        except mc.Error as e:
            self.label_result.setText("Database connection fail")
            
    def insertData(self):
        
        dbname = self.lineEdit.text()
        
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database=dbname
            )
            
            mycursor = mydb.cursor()
            
            username = self.lineEdit_username.text()
            password = self.lineEdit_password.text()
            
            query = "INSERT INTO users (username, password) VALUES (%s,%s)"
            value = (username,password)
            
            mycursor.execute(query, value)
            
            mydb.commit()
            self.label_result.setText("Data inserted")
            
        except mc.Error as e:
            self.label_result.setText("Error inserting data")
#-----------------------------------------       
        
app = QApplication(sys.argv)
Window = AppWindow()
sys.exit(app.exec())