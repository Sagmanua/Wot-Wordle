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





#---------------------Check all atributos that have tanks 
#### Check for atrtributos in random tank
def get_attr(name_guess, attr):
    for world in worlds:
        if world["name"] == name_guess:
            return world.get(attr)  # безопасно вернёт None если атрибута нет
    return None






print("Hello in my app")
print("This is world for Wot")
print("Try to guess what is guess today")
print("This is list of all tanks")
show_all_names ()
while True:
    #### input of user 
    name_guess = input("Write tank name")
    
    ### Check guess of user
    if check_on_write_enter(name_guess):
        print("Name is Right wirte")
    else:
        print("Write again")
        pass
    
    # check is user write all write
    tryes = tryes + 1 
    print("This is your",tryes,"try")

    ### Check for atibutos that have chosen tank of user 
     

    # Is a guess or not 
    if name_guess != tank_of_guess:
        print("This is not this answer ")
        
    else:
        print("You win")



    