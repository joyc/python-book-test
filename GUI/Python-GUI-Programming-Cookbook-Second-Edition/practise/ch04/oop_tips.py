#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/11/0011 15:26
# @Author  : Hython.com
# @File    : oop_tips.py
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as msg
from tkinter import Menu
from tkinter import Spinbox
from time import sleep
import ch04.ToolTip as tt

GLOBAL_CONST = 42


class OOP():
    def __init__(self):         # Initializer method
        # Create instance
        self.win = tk.Tk()

        tt.create_ToolTip(self.win, 'Hello GUI')

        # Add a title
        self.win.title("Python GUI 程序设计")
        self.create_widgets()

    # 定义按钮点击事件
    def click_me(self):
        self.button.configure(text="你好啊，" + self.name.get() + ' ' + \
                         self.number_chosen.get())

    # 定义Spinbox回调函数
    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scrol.insert(tk.INSERT, value + '\n')  # 输出结果插入到文本框scrol

    # 选择项回调，单选项
    def checkCallback(self, *ignoredArgs):
        # 只能激活一个选择项
        if self.chVarUn.get(): self.check3.configure(state='disable')
        else: self.check3.configure(state='normal')
        if self.chVarEn.get(): self.check2.configure(state='disable')
        else: self.check2.configure(state='normal')

    # Radio按钮回调函数
    def radCall(self):
        radSel = self.radVar.get()
        if   radSel == 0: self.mighty2.configure(text='Blue')
        elif radSel == 1: self.mighty2.configure(text='Gold')
        elif radSel == 2: self.mighty2.configure(text='Red')

    # 进度条回调函数
    def run_progressbar(self):
        self.progress_bar["maximum"] = 100
        for i in range(101):
            sleep(0.05)
            self.progress_bar["value"] = i  # increment progressbar
            self.progress_bar.update()      # have to call update() in loop
        self.progress_bar["value"] = 0      # reset/clear progressbar

    def start_progressbar(self):
        self.progress_bar.start()

    def stop_progressbar(self):
        self.progress_bar.stop(self)

    def progressbar_stop_after(self, wait_ms=1000):
        self.win.after(wait_ms, self.progress_bar.stop)

    def usingGlobal(self):
        global GLOBAL_CONST
        print(GLOBAL_CONST)
        GLOBAL_CONST = 777
        print(GLOBAL_CONST)

    # 程序退出函数
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    ##########################################
    def create_widgets(self):
        tabControl = ttk.Notebook(self.win)          # Create Tab Control
        tab1 = ttk.Frame(tabControl)                 # Create a tab
        tabControl.add(tab1, text='标签1')            # Add the tab
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='标签2')
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text='标签3')

        tabControl.pack(expand=1, fill="both")      # Pack to make visible

        # tab1上设置labelFramer容器
        mighty = ttk.LabelFrame(tab1, text=' 流畅的 Python ')
        mighty.grid(column=0, row=0, padx=8, pady=4)

        # 在mighty容器填加label
        a_label = ttk.Label(mighty, text="输入姓名:")
        a_label.grid(column=0, row=0, sticky='W')

        # 各个label间添加间隔
        for child in mighty.winfo_children():
            child.grid_configure(padx=8)

        # 添加文本框
        self.name = tk.StringVar()
        name_entered = ttk.Entry(mighty, width=10, textvariable=self.name)
        name_entered.grid(column=0, row=1, sticky=tk.W)

        # 添加按钮
        self.button = ttk.Button(mighty, text="点击我", command=self.click_me)
        self.button.grid(column=2, row=1)

        # 添加另外一个标签
        ttk.Label(mighty, text="选择年龄：").grid(column=1, row=0)
        number = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty, width=10, textvariable=number, state='readonly')
        self.number_chosen['value'] = (20, 25, 30, 35, 40, 50)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)

        # 添加微控条
        # spin = Spinbox(mighty, from_=0, to=10, width=5, bd=4, command=_spin)   # borderwidth=bd
        self.spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=8, command=self._spin)   # borderwidth=bd
        # self.spin['values'] = (2, 6, 19, 36, 78)
        self.spin.grid(column=0, row=2)

        # 添加提示信息
        tt.create_ToolTip(self.spin, '此处是spin box')

        # 添加文本框滚动条
        scrol_w = 30
        scrol_h = 3
        self.scrol = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scrol.grid(column=0, row=3, sticky='WE', columnspan=3)

        # 添加提示信息
        tt.create_ToolTip(self.scrol, '此处是滚动条文本框')

        # 增设标签2tab来布局剩下的控件  ----------------------------------------
        self.mighty2 = ttk.LabelFrame(tab2, text=' 新的标签 ')
        self.mighty2.grid(column=0, row=0, padx=8, pady=4)

        # 三个选择按钮
        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.mighty2, text="不可选", variable=chVarDis, state='disable')
        check1.select()
        check1.grid(column=0, row=0, sticky=tk.W)

        chVarUn = tk.IntVar()
        check2 = tk.Checkbutton(self.mighty2, text="未选择", variable=chVarUn)
        check2.deselect()
        check2.grid(column=1, row=0, sticky=tk.W)

        chVarEn = tk.IntVar()
        check3 = tk.Checkbutton(self.mighty2, text="已选择", variable=chVarEn)
        check3 .select()
        check3.grid(column=2, row=0, sticky=tk.W)

        # 跟踪两个检查按钮的状态
        chVarUn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())
        chVarEn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())

        # Radiobutton Globals
        colors = ["Blue", "Gold",  "Red"]

        # create three Radiobuttons using one variable
        self.radVar = tk.IntVar()
        # 设置不存在的默认值放置初始化时候选中某按钮导致无法设置
        self.radVar.set(99)

        # Now we are creating all three Radiobutton widgets within one loop
        for col in range(3):
            curRad = tk.Radiobutton(self.mighty2, text=colors[col], variable=self.radVar,
                                    value=col, command=self.radCall)
            curRad.grid(column=col, row=1, sticky=tk.W)

        # 布局进度条到标签2Tab2
        self.progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=280, mode='determinate')
        self.progress_bar.grid(column=0, row=3, pady=2)

        # 添加三个进度条按钮控件，先添加容器
        buttons_frame = ttk.LabelFrame(self.mighty2, text=" 进度条 ")
        buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)

        # 4个进度条按钮
        ttk.Button(buttons_frame, text=" Run 进度条   ", command=self.run_progressbar).grid(column=0, row=0, sticky='W')
        ttk.Button(buttons_frame, text=" Start 进度条  ", command=self.start_progressbar).grid(column=0, row=1, sticky='W')
        ttk.Button(buttons_frame, text=" Stop immediately ", command=self.stop_progressbar).grid(column=0, row=2, sticky='W')
        ttk.Button(buttons_frame, text=" Stop after second ", command=self.progressbar_stop_after).grid(column=0, row=3, sticky='W')

        for child in buttons_frame.winfo_children():
            child.grid_configure(padx=2, pady=2)

        for child in self.mighty2.winfo_children():
            child.grid_configure(padx=8, pady=2)

        # Tab3设置canvas控件
        tab3_frame = tk.Frame(tab3, bg='blue')
        tab3_frame.pack()
        for orange_color in range(2):
            canvas = tk.Canvas(tab3_frame, width=150, height=80,
                               highlightthickness=0, bg='orange')
            canvas.grid(row=orange_color, column=orange_color)

        # 添加菜单栏
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        # 添加菜单项目名
        # add_cascade 在垂直上加菜单
        file_menu = Menu(menu_bar, tearoff=0)   # tearoff去除第一条虚线
        file_menu.add_command(label='新建')
        file_menu.add_separator()
        file_menu.add_command(label='退出', command=self._quit)
        menu_bar.add_cascade(label="文件", menu=file_menu)

        # 显示提示文本信息
        def _msgBox():
            msg.showinfo('版本信息：', 'Python GUI 程序设计示例:\n\nHython.com @2019.')

        # 横向并列添加第二个菜单
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="关于",command=_msgBox)
        menu_bar.add_cascade(label="帮助", menu=help_menu)

        # 设置程序ico图标
        self.win.iconbitmap('pyc.ico')

        # 测试拿到spin的str
        strData = self.spin.get()
        print("Spinbox 的值: " + strData)
        # call
        self.usingGlobal()
        # 放置焦点
        name_entered.focus()

#======================
# Start GUI
#======================
oop = OOP()
oop.win.mainloop()
