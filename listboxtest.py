# example stolen from https://pythonbasics.org/tkinter-listbox/

import tkinter as tk
 
window = tk.Tk()
window.title('My Window')
 
window.geometry('500x300')
 
var1 = tk.StringVar()
l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var1)
l.pack()
 
def print_selection():
    value = lb.get(lb.curselection())   
    var1.set(value)  
 
b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()
 
var2 = tk.StringVar()
# var2.set((1,2,3,4))
# var2.set(("aasdasd",2,3,4))

examplelist = ["this","is","example","list"]

var2.set(examplelist)
lb = tk.Listbox(window, listvariable=var2)
lb.pack()
 
window.mainloop()