import tkinter as tk
from tkinter import ttk

# -------------------------
# MAIN ROOT WINDOW
# -------------------------
root = tk.Tk()
root.title("Tkinter Widgets Example")

# -------------------------
# ENTRY BOX SECTION
# -------------------------
tk.Label(root, text="First Name").grid(row=0, column=0, padx=10, pady=5)
e1 = tk.Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)

# -------------------------
# LISTBOX + SCROLLBAR
# -------------------------
frame_list = tk.Frame(root)
frame_list.grid(row=1, column=0, columnspan=2, pady=10)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

mylist = tk.Listbox(frame_list, yscrollcommand=scrollbar.set, width=40, height=10)
mylist.pack(side=tk.LEFT, fill=tk.BOTH)

for line in range(100):
    mylist.insert(tk.END, f"This is line number {line}")

scrollbar.config(command=mylist.yview)

# -------------------------
# COMBOBOX SECTION
# -------------------------
def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

label = tk.Label(root, text="Selected Item: ")
label.grid(row=2, column=0, columnspan=2, pady=10)

combo_box = ttk.Combobox(root, 
                         values=["Option 1", "Option 2", "Option 3"], 
                         state='readonly')
combo_box.grid(row=3, column=0, columnspan=2, pady=5)

combo_box.set("Option 1")
combo_box.bind("<<ComboboxSelected>>", select)

# -------------------------
# START MAINLOOP
# -------------------------
root.mainloop()
