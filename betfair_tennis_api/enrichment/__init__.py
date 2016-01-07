from flask import jsonify
from betfair_tennis_api import app
from ..dao import site_navigation
from .. import match_path

@app.route('/api/tennisMatches')
def tennisMatches():
    betfair_tennis_nav = site_navigation.get_tennis_navigation()
    raw_match_paths = match_path.get(betfair_tennis_nav)
    enriched_matches = enrich(raw_match_paths)

    return jsonify(tennisMatches=enriched_matches)


def enrich(raw_matches):
    map(is_singles, raw_matches)
    map(is_mens, raw_matches)

    return raw_matches


def is_singles(match):
    if not is_singles_by_path(match['path'][:-1]):
        match['singles'] = False
        return match

    if not is_singles_by_name(match['path'][-1]):
        match['singles'] = False
        return match

    match['singles'] = True
    return match


def is_singles_by_name(match_name):
    if match_name.count('/') == 2:
        return False

    return True


def is_singles_by_path(match):
    for p in match:
        if p == "Doubles Matches":
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
