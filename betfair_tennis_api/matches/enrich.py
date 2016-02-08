def do(raw_match_paths):
    map(split_names, raw_match_paths)

    return raw_match_paths


def split_names(raw_match):
    match_name = raw_match['path'][-1]
    match_players = match_name.split(' v ')
    
    raw_match['playerOne'] = match_players[0]
    raw_match['playerTwo'] = match_players[1]

    return raw_match
