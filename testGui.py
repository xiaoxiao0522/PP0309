import tkinter as tk
from tkinter import *

window = tk.Tk()
# foreground: Set the background color to black, short for fg
# background: Set the text color to white, short for bg

# use Label
label = tk.Label(window,
                 text="hello first gui program",
                 foreground="white",
                 background="#34A2FE",
                 width=25,
                 height=5
                 )

# draw a label in grid
# label.grid(row=0, column=0, sticky=E+W)
label.pack()

'''
#use Button
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="red",
)

button.pack()

# use Entry
entry = tk.Entry(fg="black", bg="snow2", width=50)
entry.pack()
'''
window.mainloop()
