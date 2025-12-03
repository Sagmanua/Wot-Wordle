import tkinter as tk
from tkinter import ttk
import json
import random

### variables
selected_value = None
tryes = 0


damage_guess = 0
speed_guess = 0
nacio_guess = None
class_guess = None


# load json
with open("tanks.json", "r") as file:
    worlds = json.load(file)

#### Take random tank 
nummber = random.randrange(len(worlds))
tank_of_guess = worlds[nummber]["name"]
print(tank_of_guess)

# Speed ranks 
speed_rank = {
    "veryslow": 1,
    "slow": 2,
    "medium": 3,
    "fast": 4,
    "superfast": 5
}

def get_attr(tank_of_guess, attr):
    for world in worlds:
        if world["name"] == tank_of_guess:
            return world.get(attr)  
    return None

damage_random_tank = get_attr(tank_of_guess, "damage")
speed_random_tank = get_attr(tank_of_guess, "speed")
class_random_tank = get_attr(tank_of_guess, "Class")
nacio_random_tank = get_attr(tank_of_guess,"nacio")
print(damage_random_tank,speed_random_tank,class_random_tank)





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
    get_attr_combox_damage()
    get_attr_combox_speed()
    get_attr_combox_nacio()
    get_attr_combox_class()

    Check_atributos_damage()
    Check_atributos_nacio()
    Check_atributos_Speed()
    Check_atributos_class()


#---------------Take datos from COMBOBOX

    
    
def get_attr_combox_damage():
    global selected_value, damage_guess
    damage_guess = get_attr(selected_value, "damage")
    print(damage_guess)

    return damage_guess

def get_attr_combox_speed():
    global selected_value, speed_guess
    speed_guess = get_attr(selected_value, "speed")
    print(speed_guess)
    return speed_guess

def get_attr_combox_nacio():
    global selected_value, nacio_guess
    nacio_guess = get_attr(selected_value, "nacio")
    print(nacio_guess)
    return nacio_guess

def get_attr_combox_class():
    global selected_value, class_guess
    class_guess = get_attr(selected_value, "Class")
    print(class_guess)
    return class_guess

    

#--------------------Compare atributos 
### Compare bu damage
def Check_atributos_damage ():
    global damage_guess
    global damage_random_tank
    damage_guess = int(damage_guess)
    damage_random_tank = int(damage_random_tank)
    if damage_random_tank == damage_guess:
        return("Damage the same")
    elif damage_random_tank>damage_guess:
        return print("Damage is lower")
    else:
        return print("Damage is bigger")
### Compare by class
def Check_atributos_class ():
    global class_random_tank
    global class_guess
    if class_guess == class_random_tank:
        return print("This is",class_guess)
    else:
        return print("This is not",class_guess)
###Compare speed
def Check_atributos_Speed():
    global speed_random_tank, speed_guess

    s1 = speed_rank[speed_random_tank.lower()]
    s2 = speed_rank[speed_guess.lower()]

    if s1 > s2:
        print("Random tank is faster")
    elif s1 < s2:
        print("Random tank is slower")
    else:
        print("It has the same speed")

### nacio of tank
def Check_atributos_nacio():
    global nacio_random_tank
    global nacio_guess
    if nacio_random_tank == nacio_guess:
        return print("This is",nacio_guess)
    else:
        return print("This is not",nacio_guess)

####COMBOBOX
label = tk.Label(root, text="Selected Item: ")
label.grid(row=2, column=0, columnspan=2, pady=10)

combo_box = ttk.Combobox(root, 
                         values=show_all_names(),  # pass the list of names
                         state='readonly')
combo_box.grid(row=3, column=0, columnspan=2, pady=5)

combo_box.set("Chose tank")
combo_box.bind("<<ComboboxSelected>>", select)
root.title('Counting Seconds')

#### Button
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



