def do(enriched_matches):
    map(check_tournament, enriched_matches)
    map(check_players, enriched_matches)

    return enriched_matches


def check_tournament(match):
    if 'tournament' in match and match['tournament']:
        del match['path'][0]

    return match


def check_players(match):
    if 'playerOne' in match and 'playerTwo' in match:
        del match['path'][-1]

    return match
