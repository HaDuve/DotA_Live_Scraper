from src.mainRoutine import mainRoutine

# fetch the url from args if provided
# otherwise use the default url (test match)
# Example: python scraper.py https://cyberscore.live/en/matches/83399/
# Example2: python scraper.py 83399

import sys

if len(sys.argv) > 1:
    # if provided arg is of type int then it's a match id
    # otherwise it's a url
    if sys.argv[1].isdigit():
        url = f"https://cyberscore.live/en/matches/{sys.argv[1]}/"
    else:
        url = sys.argv[1]
else:
    url = "https://cyberscore.live/en/matches/83399/"


mainRoutine(url)
