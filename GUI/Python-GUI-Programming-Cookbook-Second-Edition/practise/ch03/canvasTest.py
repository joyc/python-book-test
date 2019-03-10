'''
Mar 2019
@author: Hython.com
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from time import sleep

#==============================================
class ToolTip():
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        "显示文本提示信息"
        if self.tip_window or not tip_text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")          # get size of widget
        x = x + self.widget.winfo_rootx() + 25              # calculate to display tooltip
        y = y + cy + self.widget.winfo_rooty() + 25         # below and to the right
        self.tip_window = tw = tk.Toplevel(self.widget)     # create new tooltip window
        tw.wm_overrideredirect(True)                        # remove all Window Manager (wm) decorations
#         tw.wm_overrideredirect(False)                     # uncomment to see the effect
        tw.wm_geometry("+%d+%d" % (x, y))                   # create window size

        label = tk.Label(tw, text=tip_text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()


#===================================================================
def create_ToolTip(widget, text):
    toolTip = ToolTip(widget)       # create instance of class
    def enter(event):
        toolTip.show_tip(text)
    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>', enter)   # bind mouse events
    widget.bind('<Leave>', leave)

#==========================================

win = tk.Tk()                           # Create instance
win.title("Python GUI 程序设计")         # Add a title
tabControl = ttk.Notebook(win)          # Create Tab Control
tab1 = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab1, text='标签1')      # Add the tab
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='标签2')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='标签3')
tabControl.pack(expand=1, fill="both")  # Pack to make visible

# LabelFrame using tab1 as the parent
mighty = ttk.LabelFrame(tab1, text=' 流畅的 Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

# Label using mighty as the parent
a_label = ttk.Label(mighty, text="输入姓名:")
a_label.grid(column=0, row=0, sticky='W')

# # Add another label
# ttk.Label(mighty, text="选择年龄:").grid(column=1, row=0)

# Add some space around each label
for child in mighty.winfo_children():
    child.grid_configure(padx=8)


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

# Add another label
ttk.Label(mighty, text="选择年龄：").grid(column=1, row=0)
number = tk.StringVar()
# number_chosen = ttk.Combobox(win, width=10, textvariable=number)
number_chosen = ttk.Combobox(mighty, width=10, textvariable=number, state='readonly')
number_chosen['value'] = (20, 25, 30, 35, 40, 50)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)


# Spinbox callback
def _spin():
    value = spin.get()
    print(value)
    scrol.insert(tk.INSERT, value + '\n')    # 输出结果插入到文本框scrol


# 添加微控条
# spin = Spinbox(mighty, from_=0, to=10, width=5, bd=4, command=_spin)   # borderwidth=bd
spin = Spinbox(mighty, values=(2, 6, 19, 36, 78), width=5, bd=8, command=_spin)   # borderwidth=bd
spin.grid(column=0, row=2)

# 再添加一个spinbox
# spin = Spinbox(mighty, values=(0, 50, 100), width=5, bd=20, command=_spin)  # default value is: tk.SUNKEN
# spin = Spinbox(mighty, values=(0, 50, 100), width=5, bd=20, command=_spin, relief=tk.FLAT)
# spin = Spinbox(mighty, values=(0, 50, 100), width=5, bd=20, command=_spin, relief=tk.RAISED)
# spin = Spinbox(mighty, values=(0, 50, 100), width=5, bd=20, command=_spin, relief=tk.SUNKEN) # default
# spin = Spinbox(mighty, values=(0, 50, 100), width=5, bd=20, command=_spin, relief=tk.GROOVE)
spin = Spinbox(mighty, values=(0, 50, 100), width=5, bd=8, command=_spin, relief=tk.RIDGE)
spin.grid(column=1, row=2)

# 添加提示信息
create_ToolTip(spin, '此处是spin box')

# 添加文本框滚动条
scrol_w = 30
scrol_h = 3
scrol = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scrol.grid(column=0, row=3, sticky='WE', columnspan=3)

# 添加提示信息
create_ToolTip(scrol, '此处是滚动条文本框')

# 增设标签2tab来布局剩下的控件  ----------------------------------------
mighty2 = ttk.LabelFrame(tab2, text=' 新的标签 ')
mighty2.grid(column=0, row=0, padx=8, pady=4)

# 三个选择按钮
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="不可选", variable=chVarDis, state='disable')
check1.select()
check1.grid(column=0, row=0, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="未选择", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=0, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="已选择", variable=chVarEn)
check3 .select()
check3.grid(column=2, row=0, sticky=tk.W)


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


# Radiobutton Globals
colors = ["Blue", "Gold",  "Red"]


# Radiobutton Callback
def radCall():
    redSel = radVar.get()
    if redSel == 0: mighty2.configure(text=colors[0] + '标签')
    elif redSel == 1: mighty2.configure(text=colors[1] + '标签')
    elif redSel == 2: mighty2.configure(text=colors[2] + '标签')


# create three Radiobuttons using one variable
radVar = tk.IntVar()
radVar.set(99)  # 设置默认值放置初始化时候选中某按钮导致无法设置
# Now we are creating all three Radiobutton widgets within one loop
for col in range(3):
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar,
                            value=col, command=radCall)
    curRad.grid(column=col, row=1, sticky=tk.W)


# # 定义labels的容器LabelFrame
# buttons_frame = ttk.LabelFrame(mighty2, text=' 标签容器 ')
# buttons_frame.grid(column=1, row=7, pady=20) # padx=20, pady=40
#
# # 放置容器框架
# # ttk.Label(buttons_frame, text="标签1").grid(column=0, row=0, sticky=tk.W)
# ttk.Label(buttons_frame, text="标签1").grid(column=0, row=0, sticky=tk.W)
# ttk.Label(buttons_frame, text="标签2").grid(column=1, row=0, sticky=tk.W)
# ttk.Label(buttons_frame, text="标签3").grid(column=2, row=0, sticky=tk.W)
# # 循环给每个标签加入padx和pady
# for child in buttons_frame.winfo_children():
#     child.grid_configure(padx=8, pady=4)

# 布局进度条到标签2Tab2
progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=280, mode='determinate')
progress_bar.grid(column=0, row=3, pady=2)
# 进度条回调函数
def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i  # increment progressbar
        progress_bar.update()  # have to call update() in loop
    progress_bar["value"] = 0  # reset/clear progressbar


def start_progressbar():
    progress_bar.start()


def stop_progressbar():
    progress_bar.stop()


def progressbar_stop_after(wait_ms=1000):
    win.after(wait_ms, progress_bar.stop)

# 添加三个进度条按钮控件，先添加容器
buttons_frame = ttk.LabelFrame(mighty2, text=" 进度条 ")
buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)
# 4个进度条按钮
ttk.Button(buttons_frame, text=" Run 进度条   ", command=run_progressbar).grid(column=0, row=0, sticky='W')
ttk.Button(buttons_frame, text=" Start 进度条  ", command=start_progressbar).grid(column=0, row=1, sticky='W')
ttk.Button(buttons_frame, text=" Stop immediately ", command=stop_progressbar).grid(column=0, row=2, sticky='W')
ttk.Button(buttons_frame, text=" Stop after second ", command=progressbar_stop_after).grid(column=0, row=3, sticky='W')

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=2, pady=2)

for child in mighty2.winfo_children():
    child.grid_configure(padx=8, pady=2)


# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()

# Tab3设置canvas控件
tab3_frame = tk.Frame(tab3, bg='blue')
tab3_frame.pack()
for orange_color in range(2):
    canvas = tk.Canvas(tab3_frame, width=150, height=80,
                       highlightthickness=0, bg='orange')
    canvas.grid(row=orange_color, column=orange_color)


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

# 设置程序ico图标
win.iconbitmap('pyc.ico')

# 放置焦点
name_entered.focus()

#======================
# Start GUI
#======================
win.mainloop()
