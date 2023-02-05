# Author - Ethan Rowley - 04/02/2023

# Utility functions for main gui
from dictionary import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

USERNAMES = ['psyer2','u','u2']
PASSWORDS = ['password','p','p2']
ACCESS_LEVEL = [Admin_Access_Level,User_Access_Level,Admin_Access_Level]
# Not Set in Stone, this is a proof of concept
# 1 = Admin
# 2 = User

# A function that checks the inputted login details to our databse    
def util_try_login(username, password):
    index = 0
    check = 0
    print("OUT: ",username, password)
    while(index < len(USERNAMES)):
        if (username == USERNAMES[index] and password == PASSWORDS[index]): #Check iunputted U & P with sotred ones
            if (ACCESS_LEVEL[index] == Admin_Access_Level):
                check = Admin_Access_Level
            elif (ACCESS_LEVEL[index] == User_Access_Level):
                check = User_Access_Level
        index += 1            
    return check # check returned to the main function to decide which page to move to


# A function to add a new user to the user databse
def util_try_register():
    pass

# A class to construct graphs of a given size and return them to go in a layout frame
class MplCanvas(FigureCanvasQTAgg,):
    def __init__(self, parent=None, width=Figure_Width, height=Figure_Height, dpi = Figure_DPI):
        fig = Figure(figsize=(width,height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        
        
