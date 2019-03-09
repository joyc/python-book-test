import tkinter as tk
from tkinter import ttk


win = tk.Tk()

win.title("第一个Python GUI程序")


a_label = ttk.Label(win, text="标签A")
a_label.grid(row=0, column=0)


def click_me():
    button.configure(text="你好啊，" + name.get())


ttk.Label(win, text="输入你丫名字：").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=10, textvariable=name)
name_entered.grid(column=0, row=1)

button = ttk.Button(win, text="点击我", command=click_me)
button.grid(row=1, column=1)
# button.configure(state="disable")   # 设置按钮点击无效

# 放置焦点
name_entered.focus()

win.mainloop()
