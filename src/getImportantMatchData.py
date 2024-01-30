from src.fetchHeroNames import fetchHeroNames


def getImportantMatchData(match):
    if match is None:
        return None

    # liveMatch.keys()
    # radiant_gold_adv
    # radiant_xp_adv
    # duration
    # radiant_score
    # dire_score
    importantMatchData = {}

    # radiant_win
    # boolean or null
    # Boolean indicating whether Radiant won the match
    importantMatchData["radiant_win"] = match["radiant_win"]

    # inferred game is still in progress if radiant win is null
    importantMatchData["game_in_progress"] = match["radiant_win"] is None

    # Array of the Radiant gold advantage at each minute in the game.
    # A negative number means that Radiant is behind,
    # and thus it is their gold disadvantage.
    # importantMatchData["radiant_gold_adv"] = match["radiant_gold_adv"]

    # inferred last minute
    importantMatchData["last_radiant_gold_adv"] = match["radiant_gold_adv"][-1]

    # Array of numbers
    # Array of the Radiant experience advantage at each minute in the game.
    # A negative number means that Radiant is behind,
    # and thus it is their experience disadvantage.
    # importantMatchData["radiant_xp_adv"] = match["radiant_xp_adv"]

    # inferred last minute
    importantMatchData["last_radiant_xp_adv"] = match["radiant_xp_adv"][-1]

    # integer
    # Duration of the game in seconds
    importantMatchData["duration"] = match["duration"]
    importantMatchData["duration_min_sec"] = (
        int(match["duration"]) // 60,
        int(match["duration"]) % 60,
    )

    # integer
    # Number of kills the Radiant team had when the match ended
    importantMatchData["radiant_score"] = match["radiant_score"]

    # integer
    # Number of kills the Dire team had when the match ended
    importantMatchData["dire_score"] = match["dire_score"]

    # Array of objects
    # Array containing information on the draft. Each item contains a boolean
    # relating to whether the choice is a pick or a ban, the hero ID,
    # the team the picked or banned it, and the order.
    importantMatchData["picks_bans"] = match["picks_bans"]

    radiantDraft = []
    direDraft = []
    heroNames = fetchHeroNames()
    for pick_ban in importantMatchData["picks_bans"]:
        #  check if pick_ban["hero_id"] is in heroNames
        for hero_id, heroName in heroNames:
            if hero_id == pick_ban["hero_id"]:
                foundHeroName = heroName
        if pick_ban["is_pick"]:
            if pick_ban["team"] == 0:
                radiantDraft.append(foundHeroName)
            elif pick_ban["team"] == 1:
                direDraft.append(foundHeroName)

    importantMatchData["drafted_heros_radiant"] = radiantDraft
    importantMatchData["drafted_heros_dire"] = direDraft

    return importantMatchData
