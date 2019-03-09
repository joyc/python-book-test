import tkinter as tk
from tkinter import ttk


win = tk.Tk()

win.title("第一个Python GUI程序")

# win.resizable(False, False)

# ttk.Label(win, text="标签A").grid(column=0, row=0)

a_label = ttk.Label(win, text="标签A")
a_label.grid(row=0, column=0)


def click_me():
    button.configure(text="-- 已经被点击过 --")
    a_label.configure(foreground='red')
    a_label.configure(text="红色标签A")


button = ttk.Button(win, text="点击我", command=click_me)
button.grid(row=0, column=1)

win.mainloop()
