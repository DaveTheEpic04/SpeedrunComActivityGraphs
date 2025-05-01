import speedruncompy as srcpy
import json
import matplotlib.pyplot as plt

with open("text.json", "r") as f:
    data = json.loads(f.read())

game = "karlson_itch_io"
category = ""
isLevel = True
level = "Escape 2"

gameData = srcpy.GetGameData(gameUrl=game).perform()

game = {"Id":gameData["game"]["id"], "Name":gameData["game"]["name"]}
cats = [{"Id":cat["id"], "Name":cat["name"], "Type":cat["isPerLevel"]} for cat in gameData["categories"] if cat["archived"] == False]
levels = [{"Id":level["id"], "Name":level["name"]} for level in gameData["levels"] if level["archived"] == False]

cat = ""
for c in cats:
    if c["Name"] == category and c["Type"] == isLevel:
        cat = c["Id"]
        break

lev = ""
if isLevel:
    for l in levels:
        if l["Name"] == level:
            lev = l["Id"]
            break

months = {f"{m}/{y}":0 
          for y in range(2020, 2026)
          for m in range(1, 13)}

for d in data:
    if (cat == d["Category"] or cat == "") and (lev == d["Level"] or lev == ""):
        months[d["Date"]] += 1

plt.figure(figsize=(12, 6))
plt.plot(months.keys(), months.values(), marker='o')
plt.xticks(ticks=range(0, len(months.keys()), 6), labels=[list(months.keys())[i] for i in range(0, len(months.keys()), 6)], rotation=45)
plt.grid()
plt.xlabel("Date")
plt.ylabel("Runs")
plt.title(f"Runs of {game["Name"]}" + (f" for {category}" if category != "" else "") + (f" on {level}" if level != "" else ""))
plt.tight_layout()
plt.show()