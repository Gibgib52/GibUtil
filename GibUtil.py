"""
    GibUtil: random things i find useful bundled into one thing. also for me to learn tkinter
"""
import os
from tkinter import *
import tkinter as tk

# program stuff

utilsdir = "./Utils" # directory to scan for utilities

utillistbox = None # change scope of utillistbox

def scanUtils():
    print_debug("scanUtils: has run.")
    utilsList = [] # blank list
    for filename in os.listdir(utilsdir):
        curfile = os.path.join(utilsdir, filename) # find file from name for current iteration

        # check if it is a file
        if os.path.isfile(curfile) and curfile.endswith(".py"):
            utilsList.append(curfile)
            print_debug("scanUtils: Found " + curfile)
            
    print_debug("scanUtils: utilsList: " + str(utilsList))
    return utilsList

def launchCallback():
    print_debug("Launching {utilname}")

# prints to term and updates debuglabel
def print_debug(string):
    print(string)
    debuglabel.config(text="Debug Info: " + string)

def formatutilList(listToFormat):
    formattedlist = [] # empty list
    for i in range(len(listToFormat)): # iterate through every entry in list
        formattedlist.append(listToFormat[i].strip(utilsdir)) # strips the "./Utils" from the list entries
    return formattedlist

# add listbox with results from scanUtils()
def createUtilListbox():
    print_debug("Refreshing Listbox")
    utilsList = scanUtils() # get list of utils from scanUtils()
    utilvar = StringVar() # convert to stringvar for the listbox

    utilvar.set(formatutilList(utilsList)) # formats utilsList then sets as variable

    try:
        utillistbox.delete(0, END)  # clear listbox, if exists
    except UnboundLocalError:
        print_debug("UnboundLocalError: does not exist yet")
    except:
        print_debug("Something else went wrong 0_0")

    utillistbox = Listbox(listframe, listvariable=utilvar)
    utillistbox.pack()
    print_debug("pLp: utillistbox packed")

    utillistbox.bind('<<ListboxSelect>>', listboxSelect) # bind callback to selection change, currently unused

def listboxSelect(e):
    curselection = utillistbox.get(utillistbox.curselection()) 

# tkinter stuff
window = tk.Tk()

w = 400 # width for window
h = 280 # height for window

ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

# calculate x and y pos for centered window
calcX = ((ws/2) - (w/2)) 
calcY = ((hs/2) - (h/2))

window.geometry("{}x{}+{}+{}".format(w,h,int(calcX),int(calcY))) # set size and pos of window

window.resizable(False, False) # disables resizing
window.title("GibUtil")

utilslabel = Label(text="Python Utilities", justify="center")
utilslabel.pack()

# begin mainframe
mainframe = LabelFrame(window)

# begin listframe
listframe = LabelFrame(mainframe)

# listplaceholder = Label(listframe,text="placeholder for list of utilities")
# listplaceholder.pack()

window.after(100,createUtilListbox) # populate listpane after 100 ms (to wait for debuglabel to be loaded)

# scanbutton makes a new listbox each time you click it. unintended behavior, commented out
# scanbutton = Button(listframe,text="Scan & Update",command=refreshListbox)
# scanbutton.pack(padx="5",pady="5")

listframe.pack(side=tk.LEFT,padx=5,pady=5)

# end listframe

# begin infoframe
infoframe = LabelFrame(mainframe)

# title of currently selected utility
utiltitle = Label(infoframe,text="{utilname}") 
utiltitle.pack()

# long discription of utility
utilinfo = Message(infoframe,text="""long discription of what the utility does and how it works.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud""")
utilinfo.pack()

# button to launch currently selected utility
utillaunch = Button(infoframe, text="Launch {utilname}",command=launchCallback)
utillaunch.pack(padx=5,pady=5)

infoframe.pack(side=tk.RIGHT,padx=5,pady=5)
# end infoframe

mainframe.pack(padx=5,pady=5)
# end mainframe

# debuglabel that can be updated by calling print_debug()
debuglabel = Label(window,text="Debug Info:None")
debuglabel.pack(side=tk.RIGHT,padx=5,pady=5)

window.mainloop()