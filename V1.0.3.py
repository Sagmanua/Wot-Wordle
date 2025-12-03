import tkinter as tk
from tkinter import ttk
import json

with open("tanks.json", "r") as file:
    worlds = json.load(file)



def show_all_names():
    # Return a list of names
    return [contacto["name"] for contacto in worlds]

show_all_names()
# -------------------------
# MAIN ROOT WINDOW
# -------------------------
root = tk.Tk()
root.title("Tkinter Widgets Example")

# -------------------------
# COMBOBOX SECTION
# -------------------------
def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)



label = tk.Label(root, text="Selected Item: ")
label.grid(row=2, column=0, columnspan=2, pady=10)

combo_box = ttk.Combobox(root, 
                         values=show_all_names(),  # pass the list of names
                         state='readonly')
combo_box.grid(row=3, column=0, columnspan=2, pady=5)

combo_box.set("Chose tank")
combo_box.bind("<<ComboboxSelected>>", select)

# -------------------------
# START MAINLOOP
# -------------------------
root.mainloop()
