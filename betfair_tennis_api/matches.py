from flask import request
from dao import site_navigation


def get_tennis_matches():
    tennis_nav = site_navigation.get_tennis_navigation()
    matches = flatten_matches(tennis_nav['children'])

    matchTypeQuery = request.args.get('matchType')
    filtered_matches = filter(lambda x: filter_matches(x, 'matchType', matchTypeQuery), matches)
    matchGenderQuery = request.args.get('matchGender')
    filtered_matches = filter(lambda x: filter_matches(x, 'matchGender', matchGenderQuery), filtered_matches)

    return filtered_matches


def flatten_matches(nav_items):
    matches = []
    for nav_item in nav_items:
        tournament_name = nav_item['name']
        tournament_matches = process_tournament(tournament_name, nav_item['children'])
        if tournament_matches:
            matches.extend(tournament_matches)

    return matches


def process_tournament(tournament_name, tournament_groups):
    tournament_matches = []
    matchGender = determine_gender(tournament_name, tournament_groups)
    for group in filter(is_market, tournament_groups):
        for child in group['children']:
            if child_is_match(child):
                tournament_matches.append({
                    "tournamentName": tournament_name,
                    "name": child['name'],
                    "id": child['id'],
                    "matchUrl": request.url_root + "betfair-tennis-api/tennisMatches/" + child['id'],
                    "matchType": determine_match_type(child['name']),
                    "matchGender": matchGender
                })

    return tournament_matches


def determine_gender(tournament_name, tournament_groups):
    known_male_tournaments = ["Challenger", "ATP"]
    for known in known_male_tournaments:
        if known in tournament_name:
            return "MALE"

    return "UNKOWN"


def determine_match_type(match_name):
    if match_name.count('/') == 2:
        return 'Doubles'

    return 'Singles'


def is_market(item):
    if str(item['type']) == 'MARKET':
        return False

    return True


def child_is_match(child):
    if 'children' in child:
        for child_market in child['children']:
            if 'marketType' in child_market and child_market['marketType'] == "MATCH_ODDS":
                return True


def filter_matches(match, key, matchType):
    if matchType is None:
        return True

    if match[key] == matchType:
        return True

    return False
