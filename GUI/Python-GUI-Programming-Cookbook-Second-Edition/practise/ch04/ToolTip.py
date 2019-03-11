#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/11/0011 15:26
# @Author  : Hython.com
# @File    : ToolTip.py
import tkinter as tk


class ToolTip():
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        """显示文本提示信息"""
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


def create_tooltip(widget, text):
    toolTip = ToolTip(widget)       # create instance of class

    def enter(event):
        try: toolTip.show_tip(text)
        except: pass

    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>', enter)   # bind mouse events
    widget.bind('<Leave>', leave)
