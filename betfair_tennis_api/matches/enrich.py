mens_list = ['Men ', 'Men\'s', 'Mens']
womens_list = ['Women ', 'Women\'s', 'Womens']


def do(raw_match_paths):
    map(add_player_names, raw_match_paths)
    map(add_tournament, raw_match_paths)
    map(add_singles, raw_match_paths)
    map(add_mens, raw_match_paths)

    return raw_match_paths


def add_player_names(raw_match):
    match_name = raw_match['path'][-1]
    match_players = match_name.split(' v ')

    raw_match['playerOne'] = match_players[0]
    raw_match['playerTwo'] = match_players[1]

    return raw_match


def add_tournament(raw_match):
    raw_match['tournament'] = raw_match['path'][0]

    return raw_match


def add_singles(raw_match):
    is_singles = True
    if raw_match['path'][-1].count('/') == 2:
        is_singles = False

    raw_match['singles'] = is_singles

    return raw_match


def add_mens(raw_match):
    for p in raw_match['path']:
        if any(word in p for word in mens_list):
            raw_match['mens'] = True
            break
        elif any(word in p for word in womens_list):
            raw_match['mens'] = False
            break
        else:
            raw_match['mens'] = None

    return raw_match
