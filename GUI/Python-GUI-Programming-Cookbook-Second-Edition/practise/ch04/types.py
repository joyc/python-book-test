'''
Mar 2019
@author: Hython.com
'''
# 各数据类型遵循setget方法，取值需要用get方法才会显示默认值
#======================
# imports
#======================

import tkinter as tk

# Create instance of tkinter
win = tk.Tk()

# Create DoubleVar
doubleData = tk.DoubleVar()
print(doubleData.get())
doubleData.set(2.365)
print(doubleData.get(), type(doubleData))

add_doubles = 1.222222222222222222222 + doubleData.get()
print(add_doubles, type(add_doubles))

# Assign tkinter Variable to strData variable
strData = tk.StringVar()

# Set strData variable
strData.set('Hello StringVar')

# Get value of strData variable
varData = strData.get()

# Print out current value of strData
print(varData)