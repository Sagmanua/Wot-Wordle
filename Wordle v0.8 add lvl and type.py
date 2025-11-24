import random
import json

#use json

import json

with open("tanks.json", "r") as file:
    worlds = json.load(file)


#Declara variables
tryes = 0

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



def check_on_write_enter ():
    for world in worlds:
        if world["name"] == name_guess:
            return True
    return False


def show_all_names ():
        for i,contacto  in enumerate(worlds):
            print(i ,contacto["name"])





#---------------------Check all atributos that have tanks 
#### Check for atrtributos in random tank
def get_attr(name_guess, attr):
    for world in worlds:
        if world["name"] == name_guess:
            return world.get(attr)  
    return None

def get_attr_of_random_tank(tank_of_guess, attr):
    for world in worlds:
        if world["name"] == tank_of_guess:
            return world.get(attr)  
    return None

damage_random_tank = get_attr_of_random_tank(tank_of_guess, "damage")
speed_random_tank = get_attr_of_random_tank(tank_of_guess, "speed")
class_random_tank = get_attr_of_random_tank(tank_of_guess, "Class")
nacio_random_tank = get_attr_of_random_tank(tank_of_guess,"nacio")
print(damage_random_tank,speed_random_tank,class_random_tank)

#--------------------Compare atributos 
### Compare bu damage
def Check_atributos_damage (damage_random_tank,damage_guess):
    if damage_random_tank == damage_guess:
        return("Damage the same")
    elif damage_random_tank>damage_guess:
        return("Damage is lower")
    else:
        return("Damage is bigger")
### Compare by class
def Check_atributos_class (class_guess,class_random_tank):
    if class_guess == class_random_tank:
        return ("This is",class_guess)
    else:
        return("This is not",class_guess)
###Compare speed
def Check_atributos_Speed(speed_guess,speed_random_tank):
    s1 = speed_rank[speed_random_tank.lower()]
    s2 = speed_rank[speed_guess.lower()]

    if s1 > s2:
        return "Random tank is faster"
    elif s1 < s2:
        return "Random tank is slower"
    else:
        return "It has the same speed"
### nacio of tank
def Check_atributos_nacio(nacio_guess,nacio_random_tank, ):
    if nacio_random_tank == nacio_guess:
        return ("This is",nacio_guess)
    else:
        return("This is not",nacio_guess)


print("Hello in my app")
print("This is world for Wot")
print("Try to guess what is guess today")
print("This is list of all tanks")
show_all_names ()






while True:
    #### input of user 
    name_guess = input("Write tank name")
    
    ### Check guess of user
    if check_on_write_enter():
        print("Name is Right wirte")
    else:
        print("Write again")
        pass
    
    # check is user write all write
    tryes = tryes + 1 
    print("This is your",tryes,"try")

    ### Check for atibutos that have chosen tank of user 
    damage_guess = get_attr(name_guess, "damage")
    speed_guess = get_attr(name_guess, "speed")
    class_guess = get_attr(name_guess,"Class")
    nacio_guess = get_attr(name_guess,"nacio")
    print("Damage of tank that you guess",damage_guess)
    print("Speed of tank that you guess",speed_guess)
    print("Speed of tank that you guess",class_guess)
    print("Nacionality of the tank you guess",nacio_guess)

    # Compare random tank and that user chose
    print(Check_atributos_damage(damage_guess,damage_random_tank))
    print(Check_atributos_class(class_guess,class_random_tank))
    print(Check_atributos_Speed(speed_guess,speed_random_tank))
    print(Check_atributos_nacio(nacio_guess,nacio_random_tank))
    # Is a guess or not 
    if name_guess != tank_of_guess:
        print("This is not this answer ")
        
    else:
        print("You win")
        break



    