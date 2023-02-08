#  pyuic6 -x main_ui.ui -o main_ui.py
from main_ui import * # Python version of the UI file for welcome page
from utility import *
from dictionary import *
from dataCleaner import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QTableWidgetItem
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
        x1 = [0,1,2,3,4]
        x2 = ['A','B','C','D','E']
        y1 = [50,200,140,110,65]
        y2 = [20,15,20,50,40]
        #///////////////////\\\\\\\\\\\\\\\\\\\\
        
        lineGraph = MplCanvas(self,Line_Graph,x1,y1)
        barChart = MplCanvas(self,Bar_Chart,x2,y2)
        
        layout1 = QVBoxLayout()
        layout1.addWidget(lineGraph)
        
        layout2 = QVBoxLayout()
        layout2.addWidget(barChart)
        
        self.ui.adminThreatsFrame1.setLayout(layout1)
        self.ui.adminThreatsFrame2.setLayout(layout2)

        # TODO: @ben Link to threats page

        #-------------------------------------
        #ANIMATIONS
        #-------------------------------------



    def detectPress(self, selected, deselected):
        for cell in selected.indexes():
            print("Selected Cell: ", cell.data())
            util_editStore_title(cell.data()) # Update global store
            self.openSingleResult() # open individal result page

    # Makes method global, so it can be called within user home method
    global openThreatsPage
    def openThreatsPage(self):
        self.ui.stackedWidget.setCurrentIndex(5)

        # Ethan: I am hard coding the table values so that I have full control over them
        #        and understand how the table works, please don't use the editor to add data as we will
        #        need to iterate over data to add columns in the future anyway


        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Threat","Description"])
        self.ui.tableWidget.setRowCount(10)
        # To Add a single item, TODO: put this in a loop
        item = QTableWidgetItem()
        item.setText("Test")
        self.ui.tableWidget.setItem(0,0,item)

        item = QTableWidgetItem()
        item.setText("osc hard")
        self.ui.tableWidget.setItem(1,0,item)

        item = QTableWidgetItem()
        item.setText("rip dms")
        self.ui.tableWidget.setItem(2,0,item)


        self.ui.tableWidget.selectionModel().selectionChanged.connect(self.detectPress)



        # TODO: Populate the table with hardcoded data
        # TODO: Allow table items to be clicked
        # TODO: Navigate to templateThreats page with correct data and display it
        # TODO: Implement a search with a backend filter function
        # TODO: Populate returned data into table
    def openSingleResult(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.templateTitleLabel.setText(store.title)
        self.ui.templateReturnBtn.clicked.connect(lambda: openThreatsPage(self))

    def openUserHomePage(self):
        self.ui.stackedWidget.setCurrentIndex(User_Home_Page)

        x1 = [0, 1, 2, 3, 4]
        y1 = [50, 200, 140, 110, 65]
        lineGraph = MplCanvas(self, Line_Graph, x1, y1);

        topLayout = QHBoxLayout()
        topLayout.addWidget(lineGraph)
        self.ui.frame_8.setLayout(topLayout)

        x2 = ['A','B','C','D','E']
        y2 = [20,15,20,50,40]
        barGraph = MplCanvas(self, Bar_Chart, x2, y2)
        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(barGraph)
        self.ui.frame_9.setLayout(bottomLayout)


        # navigate to threats page from user overview
        self.ui.threatstbn.clicked.connect(lambda: openThreatsPage(self))


        #-------------------------------------
        #ANIMATIONS
        #-------------------------------------




    # Checks if the details inputted by the user on the login page are valid or not, and takes the user to the corresponding page if they are.
    def checkLoginDetails(self):
        loginResult = util_try_login(self.ui.usernameLoginLineEdit.text(), self.ui.passwordLoginLineEdit.text())        
        # Decides which page index to send the user to next depending on the result of the login check function
        if(loginResult == Admin_Access_Level):
            print("Access granted - Admin Login")
            self.changePage(Login_Page,Admin_Home_Page)
        elif(loginResult == User_Access_Level):
            print("Access granted - Admin User")
            self.changePage(Login_Page, User_Home_Page)
        else:
            print("Access Denied - Incorrect username or password detected")


# Running the program
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())