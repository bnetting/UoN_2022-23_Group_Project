# Author - Ethan Rowley - 04/02/2023

# Utility functions for main gui
from dictionary import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import store
from matplotlib.widgets import Cursor
import numpy as np
import mplcursors

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

    
# A class to construct graphs of a given size and return them to go in a layout frame
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, typeOfGraph=int,xAxes=list,yAxes=list):     

        def chart_hover(event):
            pass
            
        fig = Figure(figsize=(Figure_Width,Figure_Height), dpi=Figure_DPI)    
        ax = fig.add_subplot(111)
        
        if(typeOfGraph == Line_Graph):
            ax.plot(xAxes,yAxes,linewidth=2)
            ax.set_title("Test Line Graph")
            test = 1
            
        elif(typeOfGraph == Bar_Chart):
            ax.bar(xAxes,yAxes)
            ax.set_title("Test Bar Chart")
            test = 2
            
        elif(typeOfGraph == Pie_Chart):
            ax.pie(yAxes, labels=xAxes, explode=[0.035,0.035],autopct='%1.1f%%',shadow=True)
            ax.set_title("Test Pie Chart")
            test=3
                
        # Parses the graph ID to the motion notification function in order to tell that function x & y coordinates of a cursor on a graph,
        # and also which graph the cursor is hovering over. Maybe adding the axes and additional info being parsed in the future.
        fig.canvas.mpl_connect("motion_notify_event",lambda event: chart_hover(event))
        
        crs = mplcursors.cursor(ax,hover=2)

        @crs.connect("add")
        def _(sel):
            if(typeOfGraph == Line_Graph):
                sel.annotation.set_text('[{},{}]'.format(round(sel.target[0],2),round(sel.target[1],2)))
            elif(typeOfGraph == Bar_Chart):
                sel.annotation.set_text('{}'.format(round(sel.target[1],2)))
            sel.annotation.get_bbox_patch().set(fc="white", alpha=1)
            sel.annotation.arrow_patch.set(arrowstyle="simple", fc="black", alpha=.25)            
        
        super(MplCanvas, self).__init__(fig)
        

    