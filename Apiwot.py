import requests
import json

API_KEY = "02a11c34c34f9a3f73766e3646a1e21a"
URL = "https://api.worldoftanks.eu/wot/encyclopedia/vehicles/"

params = {
    "application_id": API_KEY,
    "language": "ru"
}

response = requests.get(URL, params=params)
data = response.json()

if data.get("status") != "ok":
    print("Ошибка API:", data)
    exit()

tanks = data["data"]

result = []

for tank in tanks.values():
    result.append({
        "name": tank["name"],
        "nation": tank["nation"],
        "type": tank["type"],
        "tier": tank["tier"]
    })

with open("tanks_simple.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Готово! Танков: {len(result)}")
