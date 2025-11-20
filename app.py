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
nummber = random.randrange(len(worlds))
print(nummber)
name_guess = "e100"
def atrtributos_gue(name_guess):
    for world in worlds:
        if world["name"] == name_guess:
            return world["atrtributos"]   # return the attribute if found
    return None  # if name not found




atrtributos_guess = atrtributos_gue(name_guess)
print(atrtributos_guess)


if name_guess == worlds[nummber]["name"]:
    print("true")
else:
    print("false")