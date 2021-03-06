import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

win = tk.Tk()

win.title("第一个Python GUI程序")


# 顶级层画布
mighty = ttk.LabelFrame(win, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

# 'NSWE' 等同于 sticky=(tk.N, tk.S, tk.W, tk.E)
# sticky='WE' ==  sticky=(tk.W, tk.E)

a_label = ttk.Label(mighty, text="输入你丫名字：")
a_label.grid(column=0, row=0, sticky='W')


def click_me():
    button.configure(text="你好啊，" + name.get() + ' ' + \
                     number_chosen.get())


# 添加文本框
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=10, textvariable=name)
name_entered.grid(column=0, row=1, sticky=tk.W)
# 添加按钮
button = ttk.Button(mighty, text="点击我", command=click_me)
button.grid(column=2, row=1)
# button.configure(state="disable")   # 设置按钮点击无效


ttk.Label(mighty, text="选择一个数字：").grid(column=1, row=0)
number = tk.StringVar()
# number_chosen = ttk.Combobox(win, width=10, textvariable=number)
number_chosen = ttk.Combobox(mighty, width=10, textvariable=number, state='readonly')
number_chosen['value'] = (1, 2, 4, 6, 22, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# 三个选择按钮
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text="不可选", variable=chVarDis, state='disable')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text="未选择", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty, text="已选择", variable=chVarEn)
check3 .select()
check3.grid(column=2, row=4, sticky=tk.W)


# 选择项回调，单选项
def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get(): check3.configure(state='disable')
    else: check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disable')
    else: check2.configure(state='normal')


# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())

# 文本框滚动条
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
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
    curRad = tk.Radiobutton(mighty, text=colors[col], variable=radVar,
                            value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)


# 定义labels的容器LabelFrame
buttons_frame = ttk.LabelFrame(mighty, text=' 标签框架 ')
buttons_frame.grid(column=1, row=7, pady=20) # padx=20, pady=40

# 放置容器框架
# ttk.Label(buttons_frame, text="标签1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="标签1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="标签2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="标签3").grid(column=2, row=0, sticky=tk.W)
# 循环给每个标签加入padx和pady
for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)


# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()


# 添加菜单栏
menu_bar = Menu(win)
win.config(menu=menu_bar)

# 添加菜单项目名
# add_cascade 在垂直上加菜单
file_menu = Menu(menu_bar, tearoff=0)   # tearoff去除第一条虚线
file_menu.add_command(label='新建')
file_menu.add_separator()
file_menu.add_command(label='退出', command=_quit)
menu_bar.add_cascade(label="文件", menu=file_menu)
# 横向并列添加第二个菜单
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="帮助", menu=help_menu)
help_menu.add_command(label="关于")

# 放置焦点
name_entered.focus()
# Start GUI
win.mainloop()
