from tkinter import *
from tkinter.font import families

root = Tk()
thelable = Label(
    root, 
    text='Hi how are you doing?', 
    height=200, 
    width=200,
    foreground='blue',
    background='black'
)
thelable.clipboard_append(root)
thelable.pack()

root.mainloop()