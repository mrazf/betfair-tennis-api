from flask import jsonify, request
from betfair_tennis_api import app
from ..dao import site_navigation
from ..player import utils


@app.route('/api/tennisMatches')
def tennisMatches():
    raw_match_paths = site_navigation.get_raw_match_paths()
    enriched_matches = enrich(raw_match_paths)
    filtered_matches = filter_matches(enriched_matches)

    result = {
        'tennisMatches': filtered_matches,
        'metadata': {
            'totalMatchesCount': len(raw_match_paths),
            'filteredMatchesCount': len(filtered_matches)
        }
    }

    return jsonify(result)


def filter_matches(matches):
    singles = json_bool_conversion(request.args.get('singles'))
    if singles:
        matches = filter(lambda x: key_filter(x, 'singles', singles), matches)

    mens = json_bool_conversion(request.args.get('mens'))
    if mens:
        matches = filter(lambda x: key_filter(x, 'mens', mens), matches)

    return matches


def key_filter(match, key, value):
    if match[key] == value:
        return True

    return False


def json_bool_conversion(string):
    if string == "true":
        return True
    return False


def enrich(raw_matches):
    map(split_names, raw_matches)
    map(is_singles, raw_matches)
    map(is_mens, raw_matches)

    return raw_matches


def split_names(match):
    match_name = match['path'][-1]
    match_players = match_name.split(' v ')
    match['playerOne'] = {
        'name': match_players[0],
        'url': utils.build_player_url(match_players[0])
    }
    match['playerTwo'] = {
        'name': match_players[1],
        'url': utils.build_player_url(match_players[1])
    }

    return match


def is_singles(match):
    if not is_singles_by_name(match['path'][-1]):
        match['singles'] = False
        return match

    match['singles'] = True
    return match


def is_singles_by_name(match_name):
    if match_name.count('/') == 2:
        return False

    return True


def is_mens(match):
    if is_mens_by_path(match['path'][:-1]):
        match['mens'] = True
        return match

    match['mens'] = False
    return match


def is_mens_by_path(match_path):
    for p in match_path:
        if "Mens " in p:
            return True

    return False
