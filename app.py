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




### Check guess of user







#### Chech for atrtributos in random tank
def atrtributos_gue(name_guess):
    for world in worlds:
        if world["name"] == name_guess:
            return world["atrtributos"]   # return the attribute if found
    return None  # if name not found

atrtributos_guess = atrtributos_gue(tank_of_guess)
print(atrtributos_guess)



while True:
    #### input of user 
    name_guess = input("Write tank name")
    # check is user write all write
    tryes = tryes + 1 
    print("This is your",tryes,"try")
    if check_on_write_enter == True:
        print("NAme is Right wirte")
    else:
        print("Write again")
    
    # Is a guess or not 
    if name_guess != tank_of_guess:
        print("This is not this answer ")
    else:
        print("You win")



    