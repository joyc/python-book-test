# ======================
# imports
# ======================
import tkinter as tk

# create instance
win = tk.Tk()

# add a title
win.title('Python GUI')

# disable resizing the GUI by passing in False/False
win.resizable(False, False)

# enable resizing x-dimension, disable y-dimension
# win.resizable(True, False)


#======================
# Start GUI
#======================
win.mainloop()
