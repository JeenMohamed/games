from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title ('CLOCK')
def = time():
    string = strftime ('%H:%M:%S')
    label.config (text=string)
    label.after(1000, time)

label = Label (root, font=("Gilroy", fontsize = 80), background = "lightpurple". foreground = "colbalt blue")
label.pack(anchor = 'center')
time()

mainloop()
