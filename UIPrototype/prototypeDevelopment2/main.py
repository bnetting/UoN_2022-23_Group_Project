#  pyuic6 -x main_ui.ui -o main_ui.py
from main_ui import * # Python version of the UI file for welcome page
from utility import *
from dictionary import *
from dataCleaner import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout
import sys

class MainWindow(QMainWindow): #Setup code for welcome page
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow() # Puts ui_welcome_Page into variable
        self.ui.setupUi(self) # Sets up the screen

        self.nextPage = Welcome_Page #Used to tell the program which page to move to next

        self.openWelcomePage() #Runs at the start of every program, and will contain the animations for bringing the welcome screen into view

        self.ui.moveToLoginButton.clicked.connect(lambda: self.changePage(Welcome_Page,Login_Page))
        self.ui.loginPushButton.clicked.connect(lambda: self.checkLoginDetails())
        self.ui.adminToggleSideMenuButton.clicked.connect(lambda: self.toggleSideBar(self.ui.adminSidePanelFrame))
        self.ui.Menu.clicked.connect(lambda: self.toggleSideBar(self.ui.menubar))


    #Toggles a side bar between hidden and shown by changing it's width between 0 and 150
    def toggleSideBar(self,targetBar):
        currentWidth = targetBar.width()
                
        if(currentWidth == 0):
            targetBar.setMaximumWidth(150)
        else:
            targetBar.setMaximumWidth(0)
        
        
    # Function takes current and desired page indexes and calls corresponding functions
    # NOTE - Sent to close___() functions, which then call the desired open___() function.
    # self.nextPage global variable also updated for functions with multiple potential pages to possibly go to
            
    def changePage(self, currentPageIndex, nextPageIndex):
        self.nextPage = nextPageIndex
        if(currentPageIndex == Welcome_Page):
            self.closeWelcomePage()
        elif(currentPageIndex == Login_Page):
            if(nextPageIndex == Admin_Home_Page):
                self.nextPage = Admin_Home_Page
            elif(nextPageIndex == User_Home_Page):
                self.nextPage = User_Home_Page
            self.closeLoginPage()
            
            
            
    def openWelcomePage(self):
        self.ui.stackedWidget.setCurrentIndex(Welcome_Page)
        #-------------------------------------
        #ANIMATIONS - Potentially animations in a seperate file and imported as a function
        #-------------------------------------
        
    def closeWelcomePage(self):
        #-------------------------------------
        #ANIMATIONS
        #-------------------------------------        
        self.openLoginPage()
    
    def openLoginPage(self):
        self.ui.stackedWidget.setCurrentIndex(Login_Page)
        #-------------------------------------
        #ANIMATIONS
        #-------------------------------------
        
    def closeLoginPage(self):
        #-------------------------------------
        #ANIMATIONS
        #-------------------------------------
        if (self.nextPage == Admin_Home_Page):
            self.openAdminHomePage()
        elif(self.nextPage == User_Home_Page):
            self.openUserHomePage()
            
            
    def openAdminHomePage(self):
        self.ui.stackedWidget.setCurrentIndex(Admin_Home_Page)
        
        self.ui.adminSidePanelFrame.setMaximumWidth(0)

        #///////////// TEST DATA \\\\\\\\\\\\\\\
            
        sc1 = MplCanvas(self)
        sc2 = MplCanvas(self)
        
        sc1.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        sc1.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        
        layout1 = QVBoxLayout()
        layout1.addWidget(sc1)
        
        layout2 = QVBoxLayout()
        layout2.addWidget(sc2)
        
        self.ui.adminThreatsFrame1.setLayout(layout1)
        self.ui.adminThreatsFrame2.setLayout(layout2)
        #////////////////////\\\\\\\\\\\\\\\\\\\\\
        
        
        #-------------------------------------
        #ANIMATIONS
        #-------------------------------------
        
    def openUserHomePage(self):
        self.ui.stackedWidget.setCurrentIndex(User_Home_Page)
        #-------------------------------------
        #ANIMATIONS
        #-------------------------------------
        
    def checkLoginDetails(self):
        loginResult = util_try_login(self.ui.usernameLoginLineEdit.text(), self.ui.passwordLoginLineEdit.text())        
        # Decides which page index to send the user to next depending on the result of the login check function
        if(loginResult == Admin_Access_Level):
            print("To admin page!")
            self.changePage(Login_Page,Admin_Home_Page)
        elif(loginResult == User_Access_Level):
            print("To user page!")
            self.changePage(Login_Page, User_Home_Page)


# - Running the GUI
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())