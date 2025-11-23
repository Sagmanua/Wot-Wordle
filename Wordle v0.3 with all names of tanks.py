import random
worlds = [
        {
            "name": "e100",
            "atrtributos": "Heavy",
            "damage":"520",
            "speed":"Slow"
            
        },
        {
            "name":"manticora",
            "atrtributos": "Light",
            "damage":"390",
            "speed":"fast"
        },
        {
            "name": "Maus",
            "atrtributos": "Heavy",
            "damage":"520",
            "speed":"Slow"
            
        },
        {
            "name": "Ebr",
            "atrtributos": "Light",
            "damage":"390",
            "speed":"super fast"
            
        },
        {
            "name": "Is-7",
            "atrtributos": "Heavy",
            "damage":"490",
            "speed":"medium"
            
        },
        {
            "name": "T-100lt",
            "atrtributos": "LIght",
            "damage":"320",
            "speed":"fast"
            
        }
]

#Declara variables
tryes = 0

#### Take random tank 
nummber = random.randrange(len(worlds))
tank_of_guess = worlds[nummber]["name"]
print(tank_of_guess)




def check_on_write_enter ():
    for world in worlds:
        if world["name"] == name_guess:
            return True
    return False


def show_all_names ():
        for i,contacto  in enumerate(worlds):
            print(i ,contacto["name"])


show_all_names ()








#### Chech for atrtributos in random tank
def atrtributos_gue(name_guess):
    for world in worlds:
        if world["name"] == name_guess:
            return world["atrtributos"]   # return the attribute if found
    return None  # if name not found

atrtributos_guess = atrtributos_gue(tank_of_guess)
print(atrtributos_guess)


print("Hello in my app")
print("This is world for Wot")
print("Try to guess what is guess today")
while True:
    #### input of user 
    name_guess = input("Write tank name")
    
    ### Check guess of user
    if check_on_write_enter == True:
        print("NAme is Right wirte")
    else:
        print("Write again")
        pass

    # check is user write all write
    tryes = tryes + 1 
    print("This is your",tryes,"try")


    # Is a guess or not 
    if name_guess != tank_of_guess:
        print("This is not this answer ")
    else:
        print("You win")



    