import re
from bs4 import BeautifulSoup

class HeroData:
    def __init__(self, name: str, hero: str, games: int, win_rate: int):
        self.name = name
        self.hero = hero
        self.games = games
        self.win_rate = win_rate

    def __repr__(self):
        return f"(Player: {self.name}, Hero:{self.hero}, Games:{self.games}, WR%:{self.win_rate})"


def fetchDraftData(soup: BeautifulSoup):
    if not soup:
        # throw error
        return "Error: soup is null"

    # Extract the relevant data using BeautifulSoup
    draftedHeros = soup.select('.picks-item')

    # List to store extracted hero data
    hero_data_list = []

    for hero_element in draftedHeros:
        # Extract information for each hero
        player_name = hero_element.select_one('.name').text.strip()
        if hero_element.select_one('.hero-stats-in span').text != '-':
            # TODO: wait until draft is finished
            hero_games = int(hero_element.select_one('.hero-stats-in span').text.strip())
            hero_win_rate = int(hero_element.select('.hero-stats-in span')[1].text.strip('%'))
        else:
            return "Error: draft not finished?"

        # Extract hero name which is always inside of brackets like this: "(Hero Name)"
        data_tooltip_html = hero_element['data-tooltip-html']
        hero_name_match = re.search(r'\(([^)]+)\)', data_tooltip_html)
        hero_name = hero_name_match.group(1) if hero_name_match else "Unknown Hero"

        hero_data = HeroData(player_name, hero_name, hero_games, hero_win_rate)

        # Append the dictionary to the list
        hero_data_list.append(hero_data)

    return hero_data_list
