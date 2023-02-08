# Author - Ethan Rowley - 04/02/2023

# Utility functions for main gui
from dictionary import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import store

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
        if (username == USERNAMES[index] and password == PASSWORDS[index]): #Check inputted U & P with sotred ones
            if (ACCESS_LEVEL[index] == Admin_Access_Level):
                check = Admin_Access_Level
            elif (ACCESS_LEVEL[index] == User_Access_Level):
                check = User_Access_Level
        index += 1            
    return check # check returned to the main function to decide which page to move to


# A function to add a new user to the user databse
def util_try_register():
    pass


# A function to edit the value stored in store
def util_editStore_title(payload):
    store.title = payload

# A function to perform an action when the user hovers over a graph
def chart_hover(event, graphID):
    print(graphID)

# A class to construct graphs of a given size and return them to go in a layout frame
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, typeOfGraph=int,xAxes=list,yAxes=list):     

        fig = Figure(figsize=(Figure_Width,Figure_Height), dpi=Figure_DPI)    
        self.axes = fig.add_subplot(111)
        
        if(typeOfGraph == Line_Graph):
            self.axes.plot(xAxes,yAxes,marker='*')
            test = 1
            
        elif(typeOfGraph == Bar_Chart):
            self.axes.bar(xAxes,yAxes)
            test = 2
            
        # Parses the graph ID to the motion notification function in order to tell that function x & y coordinates of a cursor on a graph,
        # and also which graph the cursor is hovering over. Maybe adding the axes and additional info being parsed in the future.
        fig.canvas.mpl_connect("motion_notify_event",lambda event: chart_hover(event, test))
        
        super(MplCanvas, self).__init__(fig)    

        

        
        
