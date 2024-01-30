# fetchTeamNames.py
from bs4 import BeautifulSoup

# The `fetchTeamNames` function takes a BeautifulSoup object `soup` as input and retrieves the
# team names from the HTML using CSS selectors. It selects all elements with the class name
# "name-full" and prints the title and text of each element. Finally, it returns the list of team
# names.


def fetchTeamNames(soup: BeautifulSoup):
    if not soup:
        # throw error
        return "Error: soup is null"

    # Extract the relevant data using BeautifulSoup
    # Example: titles = soup.select('.title-class')
    teamNames = soup.select(".name-full")

    # List to store extracted hero data
    first2Names = teamNames[:2]
    # change each element to its .text value if existent
    first2Names = [name.text for name in first2Names if name.text]

    if not first2Names or len(first2Names) < 2:
        # throw error
        return "Error: first2Names is null"

    return first2Names
