from tkinter import *

root = Tk()

# Label new params:
"""
    1st = where
    2nd = what text
    3rd = bg= <- lit. 'background' what color
    4th = fg= <- lit. 'foreground' what text color 
"""
# .pack() new params:
"""
    1st = location
    2nd = fill= <- fills the screen based on the root window's dimensions 
"""
one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)

root.mainloop()
