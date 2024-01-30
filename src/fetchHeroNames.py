import requests


def fetchHeroNames():
    # TODO: save locally and check for updates
    response = requests.get("https://api.opendota.com/api/heroes")
    if response.status_code != 200:
        print("Error, status code: ", response.status_code)
        return None
    heroes = response.json()

    if not heroes:
        print("Error, invalid data")
        return None

    tupleOfIdsAndHeroNames = []
    for hero in heroes:
        tupleOfIdsAndHeroNames.append((hero["id"], hero["localized_name"]))

    if tupleOfIdsAndHeroNames:
        print("found", len(tupleOfIdsAndHeroNames), "heroes")
        return tupleOfIdsAndHeroNames

    print("Error, no hero-names found")
    return None
