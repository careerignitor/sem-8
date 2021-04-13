from tkinter import *
from random import choice

win = Tk()  ## win is a top or parent window


C = Canvas(win, height=250, width=250)

b = Button(win, text="red", command=lambda: C.configure(bg="red"))
b.configure(width = 10, activebackground = "red", relief = FLAT)


C.pack()
b.pack()

win.mainloop()