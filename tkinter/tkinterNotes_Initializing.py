from tkinter import *

# anytime I see root, just think blank window
root = Tk()

# anytime I want to create text in tkinter, it's called a label
# Label params:
"""
    1st = location where you want to put it
    2nd = str, the text
"""
theLabel = Label(root, text="This is easy")

# packs everything together
theLabel.pack()

# the starter is a loop because GUIs need to be on the screen until
#   the user wants to quit out of it. 
root.mainloop()


# basic framework for tkinter program, just copy and paste:
"""
from tkinter import *

root = Tk()

# new code goes here

root.mainloop()
"""