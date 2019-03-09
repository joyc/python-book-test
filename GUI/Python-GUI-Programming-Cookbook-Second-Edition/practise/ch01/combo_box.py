import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


win = tk.Tk()

win.title("第一个Python GUI程序")


a_label = ttk.Label(win, text="标签A")
a_label.grid(row=0, column=0)


def click_me():
    button.configure(text="你好啊，" + name.get() + ' ' + \
                     number_chosen.get())


ttk.Label(win, text="输入你丫名字：").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=10, textvariable=name)
name_entered.grid(column=0, row=1)

button = ttk.Button(win, text="点击我", command=click_me)
button.grid(row=1, column=2)
# button.configure(state="disable")   # 设置按钮点击无效


ttk.Label(win, text="选择一个数字：").grid(column=1, row=0)
number = tk.StringVar()
# number_chosen = ttk.Combobox(win, width=10, textvariable=number)
number_chosen = ttk.Combobox(win, width=10, textvariable=number, state='readonly')
number_chosen['value'] = (1, 2, 4, 6, 22, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# 三个选择按钮
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="不可选", variable=chVarDis, state='disable')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="未选择", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="已选择", variable=chVarEn)
check3 .select()
check3.grid(column=2, row=4, sticky=tk.W)

# Radiobutton Globals
COLOR1 = "蓝色"
COLOR2 = "Gold"
COLOR3 = "红色"


# Radiobutton Callback
def radCall():
    redSel = radVar.get()
    if redSel == 1: win.configure(background='blue')
    elif redSel == 2: win.configure(background=COLOR2)
    elif redSel == 3: win.configure(background='red')

# create three Radiobuttons using one variable
radVar = tk.IntVar()

rad1 = tk.Radiobutton(win, text=COLOR1,  variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text=COLOR2,  variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(win, text=COLOR3,  variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

# 文本框滚动条
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# 放置焦点
name_entered.focus()

win.mainloop()
