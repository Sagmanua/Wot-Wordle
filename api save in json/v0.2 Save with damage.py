import requests
import json

API_KEY = "02a11c34c34f9a3f73766e3646a1e21a"
MIN_TIER = 8

# Step 1: Get all tanks (including their profiles)
URL_VEHICLES = "https://api.worldoftanks.eu/wot/encyclopedia/vehicles/"
# We add 'default_profile' to the fields to make sure we get the gun stats
params = {
    "application_id": API_KEY, 
    "language": "en",
    "fields": "name,type,tier,nation,default_profile.ammo" 
}

response = requests.get(URL_VEHICLES, params=params)
data = response.json()

if data.get("status") != "ok":
    print("API error:", data)
    exit()

tanks = data["data"]
result = []

for tank_id, tank in tanks.items():
    if tank.get("tier", 0) < MIN_TIER:
        continue

    tank_name = tank.get("name", "Unknown")
    tank_class = tank.get("type", "Unknown").capitalize()
    tank_tier = tank.get("tier", 0)
    tank_nation = tank.get("nation", "Unknown").upper()

    # Step 2: Get damage from the 'ammo' list inside the default profile
    # The 'ammo' field contains the damage values for the standard shells
    damage = 0
    default_profile = tank.get("default_profile", {})
    ammo_list = default_profile.get("ammo", [])

    if ammo_list:
        # Each shell in 'ammo' has a 'damage' list (usually 3 values for min/avg/max)
        # We want the average damage (the middle value, or index 1)
        # Or just the max value from all available shell types
        all_shell_damages = []
        for shell in ammo_list:
            shell_damage_values = shell.get("damage", [0, 0, 0])
            # Index 1 is typically the average damage for that shell
            all_shell_damages.append(shell_damage_values[1])
        
        if all_shell_damages:
            damage = max(all_shell_damages)

    result.append({
        "name": tank_name,
        "class": tank_class,
        "tier": tank_tier,
        "nation": tank_nation,
        "damage": damage
    })

# Save to JSON
with open("tanks_fixed.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"Done! Saved {len(result)} tanks. AMX 50 100 should now show 300 damage.")