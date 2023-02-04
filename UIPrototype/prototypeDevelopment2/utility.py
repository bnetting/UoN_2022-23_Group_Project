# Author - Ethan Rowley - 04/02/2023
# Utility functions for main gui

USERNAMES = ['psyer2', 'user2']
PASSWORDS = ['password', 'password2']
ACCESS_LEVEL = [1, 2]
# Not Set in Stone, this is a proof of concept
# 1 = Admin
# 2 = User

# self.pushButton_4.clicked.connect(lambda: util_try_login(self.stackedWidget,self.lineEdit_5.text(), self.lineEdit_6.text()))
# self.pushButton_5.clicked.connect(lambda: util_navigate_login(self.stackedWidget))


def util_navigate_login(stackWidget):
    stackWidget.setCurrentIndex(2)

# Ill comment this later, i am still making it
def util_try_login(stackWidget, username, password):
    print("OUT: ",username, password)
    if (username == USERNAMES[0] and password == PASSWORDS[0]):
        if (ACCESS_LEVEL[0] == 1):
            stackWidget.setCurrentIndex(4)
        elif (ACCESS_LEVEL[0] == 2):
            stackWidget.setCurrentIndex(5)
    else:
        print("Error")

def util_try_register():
    pass