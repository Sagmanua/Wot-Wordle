from tkinter import *

#box
master = Tk()
Label(master, text='First Name').grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
mainloop()




#Scrollbar


scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(master, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()


### Combobox
import tkinter as tk
from tkinter import ttk

def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("Combobox Example")

# Create a label
label = tk.Label(root, text="Selected Item: ")
label.pack(pady=10)

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"], state='readonly')
combo_box.pack(pady=5)

# Set default value
combo_box.set("Option 1")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", select)
root.mainloop()