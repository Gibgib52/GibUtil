"""
    GibUtil: random things i find useful bundled into one thing. also for me to learn tkinter
"""
import os
from tkinter import *
import tkinter as tk

# program stuff

utilsdir = "./Utils" # directory to scan for utilities

def scanUtils():
    print_debug("scanUtils: has run.")
    utilsList = [] # blank list
    for filename in os.listdir(utilsdir):
        file = os.path.join(utilsdir, filename) # find file from name for current iteration

        # check if it is a file
        if os.path.isfile(file) and file.endswith(".py"):
            utilsList.append(file)
            print_debug("scanUtils: Found " + file)
            
    print_debug("scanUtils: utilsList: " + str(utilsList))
    return utilsList

def launchCallback():
    print_debug("Launching {utilname}")

# prints to term and updates debuglabel
def print_debug(string):
    print(string)
    debuglabel.config(text="Debug Info: " + string)

# add listbox with results from scanUtils()
def populateListpane():
    print_debug("pLp: has run.")
    utilsList = scanUtils() # get list of utils from scanUtils()
    utilvar = StringVar() # convert to stringvar for the listbox
    utilvar.set(utilsList)

    utillistbox = Listbox(listpane, listvariable=utilvar, height=6)
    utillistbox.pack()
    print_debug("pLp: utillistbox packed")

    # utillistbox.bind('<<ListboxSelect>>', callback) # bind callback to selection change, currently unused

# tkinter stuff
window = tk.Tk()

w = 400 # width for window
h = 260 # height for window

ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

# calculate x and y pos for centered window
calcX = ((ws/2) - (w/2)) 
calcY = ((hs/2) - (h/2))

window.geometry("{}x{}+{}+{}".format(w,h,int(calcX),int(calcY))) # set size and pos of window

window.resizable(False, False) # disables resizing
window.title("GibUtil")

utilslabel = Label(text="Utilities", justify="center")
utilslabel.pack()

# begin mainframe
mainframe = LabelFrame(window)

# begin listframe
listframe = LabelFrame(mainframe)

# listplaceholder = Label(listframe,text="placeholder for list of utilities")
# listplaceholder.pack()

listpane = Frame(listframe)

window.after(100,populateListpane) # populate listpane after 100 ms (to wait for debuglabel to be loaded)

scanbutton = Button(listframe,text="Scan & Update",command=populateListpane)
scanbutton.pack(padx="5",pady="5")

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