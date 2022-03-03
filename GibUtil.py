"""
    GibUtil: random things i find useful bundled into one thing
"""
import os
from tkinter import *
import tkinter as tk

window = tk.Tk()

w = 400 # width for window
h = 250 # height for window

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

mainframe = LabelFrame(window)
# begin listframe
listframe = LabelFrame(mainframe)
listplaceholder = Label(listframe,text="placeholder for list of utilities")
listplaceholder.pack()

# list that iterates through .\Utils

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

window.mainloop()