import tkinter as tk
from tkinter import ttk
import json

### variables
selected_value = None



with open("tanks.json", "r") as file:
    worlds = json.load(file)



def show_all_names():
    # Return a list of names
    return [contacto["name"] for contacto in worlds]





def diHola():
    return print("Hola")

# -------------------------
# MAIN ROOT WINDOW
# -------------------------
root = tk.Tk()
root.title("Tkinter Widgets Example")

# -------------------------
# COMBOBOX SECTION
# -------------------------
def select(event=None):
    global selected_value
    selected_value = combo_box.get()
    label.config(text="Selected Item: " + selected_value)
    #print("Selected value:", selected_value)  # Can use this value elsewhere
    return selected_value

def print_name():
    global selected_value
    return selected_value

def combined():
    select()
    print(print_name())


label = tk.Label(root, text="Selected Item: ")
label.grid(row=2, column=0, columnspan=2, pady=10)

combo_box = ttk.Combobox(root, 
                         values=show_all_names(),  # pass the list of names
                         state='readonly')
combo_box.grid(row=3, column=0, columnspan=2, pady=5)

combo_box.set("Chose tank")
combo_box.bind("<<ComboboxSelected>>", select)


root.title('Counting Seconds')
button = tk.Button(root, text='Select', width=25, command=combined)
button.grid(row=4, column=0, columnspan=2, pady=20, padx=50)



# -------------------------
# START MAINLOOP
# -------------------------
root.mainloop()

'''
call 2 comands with lambda
button = tk.Button(root, text='Select', width=25, command=lambda: [select(), another_function()])
button.pack()



combiend 2 def in 1 
def select():
    print("Select function executed")

def another_function():
    print("Another function executed")

def combined():
    select()
    another_function()
'''



