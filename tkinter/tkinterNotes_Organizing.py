from tkinter import *

# main window object 
root = Tk()

# the frame, an invisible rectangle that can be a basic layout
topFrame = Frame(root)
bottomFrame = Frame(root)

# anytime I want something to display, I have to pack it in
# .pack() params:
"""
    1st = side=CAPS (<- what side I want), TOP is default
"""
topFrame.pack()
bottomFrame.pack(side=BOTTOM)

# widgets
# Button() params:
"""
    1st = frame where you want to put the button
    2nd = what you want to put in the button (i.e., text = submit)
    3rd = fg="aColor" <- set this equal to a color, [optional]
"""
button1 = Button(topFrame, text="click me", fg="red")
button2 = Button(topFrame, text="click me", fg="blue")
button3 = Button(topFrame, text="click me", fg="green")
button4 = Button(bottomFrame, text="click me", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()