'''
Mar 2019
@author: Hython.com
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

win = tk.Tk()                           # Create instance
win.title("Python GUI 程序设计")         # Add a title
tabControl = ttk.Notebook(win)          # Create Tab Control
tab1 = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab1, text='标签1')      # Add the tab
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='标签2')
tabControl.pack(expand=1, fill="both")  # Pack to make visible

# LabelFrame using tab1 as the parent
mighty = ttk.LabelFrame(tab1, text=' 流畅的 Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

# Label using mighty as the parent
a_label = ttk.Label(mighty, text="输入姓名:")
a_label.grid(column=0, row=0, sticky='W')

# Add another label
ttk.Label(mighty, text="选择年龄:").grid(column=1, row=0)

# Add some space around each label
for child in mighty.winfo_children():
    child.grid_configure(padx=8)

#======================
# Start GUI
#======================
win.mainloop()