"""
    GibUtil: random things i find useful bundled into one thing. also for me to learn tkinter
"""
import os
from tkinter import *
import tkinter as tk

# program stuff

utilsdir = "Utils" # directory to scan for utilities

def scanUtils():
    for filename in os.listdir(utilsdir):
        file = os.path.join(utilsdir, filename) # find file from name for current iteration
        # check if it is a file
        if os.path.isfile(file):
            DEBUG_LABEL_TEXT = file


# tkinter (GUI) stuff
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
listplaceholder = Label(listframe,text="placeholder for list of utilities")
listplaceholder.pack()

listframe.pack(side=tk.LEFT,padx=5,pady=5)
# end listframe

# begin infoframe
infoframe = LabelFrame(mainframe)

utiltitle = Label(infoframe,text="{utilname}") # title of currently selected utility
utiltitle.pack()

utilinfo = Message(infoframe,text="""long discription of what the utility does and how it works.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud""")
utilinfo.pack()

utillaunch = Button(infoframe, text="Launch {utilname}")
utillaunch.pack(padx=5,pady=5)

infoframe.pack(side=tk.RIGHT,padx=5,pady=5)
# end infoframe

mainframe.pack(padx=5,pady=5)
# end mainframe

# debug label incase i need to print something for, well debugging
try:
    debuglabel = Label(window,text="Debug Info:{}".format(DEBUG_LABEL_TEXT))
    debuglabel.pack(side=tk.RIGHT,padx=5,pady=5)
except NameError:
    debuglabel = Label(window,text="NameError: DEBUG_LABEL_TEXT is not defined (forgot to put debug?)")
    debuglabel.pack(side=tk.RIGHT,padx=5,pady=5)

window.mainloop()