import random
worlds = [
        {
            "name": "e100",
            "atrtributos": "lithe",
            "damage":"390",
            "speed":"fast"
            
        },
        {
            "name":"manticora",
            "atrtributos": "lithe",
            "damage":"390",
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




atrtributos_gue = probar(name_guess)
print(atrtributos_guess)


if name_guess == worlds[nummber]["name"]:
    print("true")
else:
    print("false")