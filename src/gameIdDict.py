def saveIdInDict(gameId, cyberId):
    # add the gameId to the dictionary
    with open("data/gameIdDict.txt", "a") as f:
        f.write(f'"{gameId}": "{cyberId}",\n')


def loadIdFromDict(cyberId):
    # create if not exists
    with open("data/gameIdDict.txt", "a") as f:
        f.write("")
    # read
    with open("data/gameIdDict.txt", "r") as f:
        for line in f:
            if line.startswith("{"):
                continue
            if line.startswith("}"):
                continue
            if line.startswith('"'):
                line = line.strip()
                line = line.strip(",")
                line = line.strip('"')
                line = line.split('": "')
                if line[1] == cyberId:
                    return line[0]
    return False
