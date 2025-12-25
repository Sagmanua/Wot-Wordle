import requests
import json

API_KEY = "02a11c34c34f9a3f73766e3646a1e21a"
MIN_TIER = 8

# Request specific fields to get speed and premium status
URL_VEHICLES = "https://api.worldoftanks.eu/wot/encyclopedia/vehicles/"
params = {
    "application_id": API_KEY, 
    "language": "en",
    "fields": "name,type,tier,nation,is_premium,default_profile.ammo,default_profile.speed_forward"
}

response = requests.get(URL_VEHICLES, params=params)
data = response.json()

if data.get("status") != "ok":
    print("API error:", data)
    exit()

tanks = data["data"]
result = []

for tank_id, tank in tanks.items():
    tier = tank.get("tier", 0)
    if tier < MIN_TIER:
        continue

    # 1. Map Name
    name = tank.get("name", "Unknown")

    # 2. Map Class (Removing 'tank' from 'Heavytank' to match your 'Light' style)
    raw_type = tank.get("type", "Unknown").capitalize()
    clean_class = raw_type.replace("tank", "")

    # 3. Calculate Damage (Average of the first shell)
    ammo = tank.get("default_profile", {}).get("ammo", [])
    damage_val = "0"
    if ammo:
        # Index 1 is the average damage
        damage_val = str(ammo[0].get("damage", [0, 0, 0])[1])

    # 4. Map Speed (Logic: >50 fast, 35-50 medium, <35 slow)
    top_speed = tank.get("default_profile", {}).get("speed_forward", 0)
    if top_speed > 50:
        speed_category = "fast"
    elif top_speed >= 35:
        speed_category = "medium"
    else:
        speed_category = "slow"

    # 5. Map Nation (Manual mapping to match your "UK" style)
    nation_map = {
        "uk": "UK",
        "usa": "USA",
        "ussr": "USSR",
        "germany": "Germany",
        "france": "France",
        "china": "China",
        "japan": "Japan",
        "czech": "Czech",
        "poland": "Poland",
        "sweden": "Sweden",
        "italy": "Italy"
    }
    nation = nation_map.get(tank.get("nation"), tank.get("nation", "Unknown").capitalize())

    # 6. Map Type (Tech-Tree vs Premium)
    is_prem = tank.get("is_premium", False)
    tank_type = "Premium" if is_prem else "Tech-Tree"

    # BUILD THE JSON OBJECT IN YOUR STYLE
    result.append({
        "name": name,
        "Class": clean_class,
        "damage": damage_val,
        "speed": speed_category,
        "nacio": nation,
        "lvl": str(tier),
        "type": tank_type
    })

# Save to JSON
with open("tanks.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print(f"Successfully saved {len(result)} tanks in your custom format!")