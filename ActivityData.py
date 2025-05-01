import speedruncompy as srcpy
import json
from datetime import datetime

def writeToJson(vals):
    with open("text.json", "w") as f:
        f.write(json.dumps(vals, indent=4))

game = "karlson_itch_io"

gameData = srcpy.GetGameData(gameUrl=game).perform()

game = (gameData["game"]["id"], gameData["game"]["name"])
cats = [{"Id":cat["id"], "Name":cat["name"]} for cat in gameData["categories"] if cat["archived"] == False]

allRuns = []

for cat in cats:
    runs = srcpy.GetGameLeaderboard2(gameId=game[0], categoryId=cat["Id"], obsolete=1).perform_all()

    allRuns = allRuns + [
        {"Category":run["categoryId"], 
         "Level":(run["levelId"] if "levelId" in run else ""), 
         "Date":f"{datetime.fromtimestamp(run["date"]).month}/{datetime.fromtimestamp(run["date"]).year}"} 
         for run in runs["runList"] 
         ]

writeToJson(allRuns)