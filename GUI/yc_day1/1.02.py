"""
Feb 2019
@author: Hython
"""
from tkinter import Tk
from tkinter import Label, Button

win =Tk()
win.title('图片地址替换助手v0.1')
my_label = Label(win, text='就是标签1')
my_button = Button(win, text='这是个按钮1')
my_label.pack()
my_button.pack()
win.mainloop()
