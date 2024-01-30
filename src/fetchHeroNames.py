import os
import json


def fetchHeroNames():
    if os.path.exists("data/heroes.json"):
        with open("data/heroes.json", "r") as f:
            print("file found!")
            ids = json.load(f)
            if ids:
                tupleOfIdsAndHeroNames = []
                for hero_id in ids:
                    tupleOfIdsAndHeroNames.append(
                        (hero_id, ids[hero_id]["localized_name"])
                    )
                return tupleOfIdsAndHeroNames
