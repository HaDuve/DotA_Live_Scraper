import requests
from bs4 import BeautifulSoup
from pprint import pprint

from src.fetchTeamNames import fetchTeamNames
from src.fetchDraftData import fetchDraftData
from src.fetchProGameIdByTeamNames import fetchProGameIdByTeamNames
from src.fetchProGameLive import fetchProGameLive
from src.getImportantMatchData import getImportantMatchData


def mainRoutine(url):
    # Send a GET request to the website
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        teamNames = fetchTeamNames(soup)
        picks = fetchDraftData(soup)
        cyberId = url.split("/")[-2].strip("/")
        gameId = fetchProGameIdByTeamNames(teamNames, cyberId)
        if gameId is not None:
            liveMatch = fetchProGameLive(gameId)
            importantMatchData = getImportantMatchData(liveMatch)

            pprint(teamNames)
            pprint(picks)
            pprint(gameId)
            pprint(importantMatchData)
        else:
            print("Failed to get game ID data.")

    else:
        print("Error: Failed to retrieve data.")
