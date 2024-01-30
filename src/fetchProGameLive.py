import requests


def fetchProGameLive(match_id):
    # /matches/{match_id}

    response = requests.get(f"https://api.opendota.com/api/matches/{match_id}")
    if response.status_code != 200:
        print("Error: fetching pro game live ", response.status_code)
        return None
    liveMatch = response.json()
    return liveMatch
