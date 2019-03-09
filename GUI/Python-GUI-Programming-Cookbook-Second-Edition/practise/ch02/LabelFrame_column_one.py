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

# 文本框滚动条
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=5, columnspan=3) # removed sticky='WE'

# Radiobutton Globals
colors = ["Blue", "Gold",  "Red"]


# Radiobutton Callback
def radCall():
    redSel = radVar.get()
    if redSel == 0: win.configure(background=colors[0])
    elif redSel == 1: win.configure(background=colors[1])
    elif redSel == 2: win.configure(background=colors[2])


# create three Radiobuttons using one variable
radVar = tk.IntVar()
radVar.set(99)  # 设置默认值放置初始化时候选中某按钮导致无法设置
# Now we are creating all three Radiobutton widgets within one loop
for col in range(3):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar,
                            value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)


# 定义labels的容器LabelFrame
buttons_frame = ttk.LabelFrame(win, text=' 标签框架 ')
buttons_frame.grid(column=1, row=7, pady=20) # padx=20, pady=40

# 放置容器框架
# ttk.Label(buttons_frame, text="标签1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="标签1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="标签2").grid(column=0, row=1, sticky=tk.W)
ttk.Label(buttons_frame, text="标签3").grid(column=0, row=2, sticky=tk.W)
# 循环给每个标签加入padx和pady
for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

# 放置焦点
name_entered.focus()
# Start GUI
win.mainloop()
