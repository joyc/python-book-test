import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title('Python GUI')

# adding a label
ttk.Label(win, text='A label').grid(column=0, row=0)

win.mainloop()