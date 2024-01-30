import requests
from src.gameIdDict import saveIdInDict, loadIdFromDict


def fetchProGameIdByTeamNames(teamNames, cyberId):
    loadIdFromDictResult = loadIdFromDict(cyberId)
    if loadIdFromDictResult:
        print("found match id in dict")
        return loadIdFromDictResult

    response = requests.get("https://api.opendota.com/api/proMatches")
    if response.status_code != 200:
        print("Error, status code: ", response.status_code)
        return None
    openDotaProMatches = response.json()

    list_of_matches = []

    if not openDotaProMatches or not teamNames or len(teamNames) != 2:
        print("Error, invalid data")
        return None

    for match in openDotaProMatches:
        # if not match["radiant_name"]:
        #     continue
        # if not match["dire_name"]:
        #     continue
        nameRadiant = (match["radiant_name"] or "").lower().strip()
        nameDire = (match["dire_name"] or "").lower().strip()
        teamNameRadiant = (teamNames[0] or "").lower().strip()
        teamNameDire = (teamNames[1] or "").lower().strip()

        if nameRadiant == teamNameRadiant or nameDire == teamNameDire:
            list_of_matches.append(match)
            saveIdInDict(match["match_id"], cyberId)
            continue
        elif nameRadiant == teamNameDire or nameDire == teamNameRadiant:
            list_of_matches.append(match)
            saveIdInDict(match["match_id"], cyberId)
            continue

    if list_of_matches:
        print("found", len(list_of_matches), "matches")
        return list_of_matches[0]
    print("Error, no matches found")
    return None
