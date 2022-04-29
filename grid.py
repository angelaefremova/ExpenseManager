from tkinter import *
from main_menu import *
from functions import *
root = Tk()

title = Label(root, text="Expense Tracker")
title.pack()
category = Button(root, text="Categories", show_categories)

root.mainloop()



