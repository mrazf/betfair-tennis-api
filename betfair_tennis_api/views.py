from flask import jsonify, request
from betfair_tennis_api import app, site_navigation

@app.route("/tennisNavigation/")
def tennis_navigation():
    return jsonify(site_navigation.get_tennis_navigation())


@app.route("/tennisMatches/")
def tennis_matches():
    tennis_nav = site_navigation.get_tennis_navigation()
    matches = flatten_matches(tennis_nav['children'])

    return jsonify(matches=matches)


@app.route("/tennisMatches/<event_id>/")
def tennis_match(event_id):
    events = site_navigation.get_tennis_event(event_id)

    return jsonify(market_catalogue=events)


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
    for group in filter(is_market, tournament_groups):
        for child in group['children']:
            if child_is_match(child):
                tournament_matches.append({
                    "tournamentName": tournament_name,
                    "name": child['name'],
                    "eventId": child['id'],
                    "matchUrl": request.url_root + "tennisMatches/" + child['id']
                })

    return tournament_matches


def is_market(item):
    if str(item['type']) == 'MARKET':
        return False

    return True


def child_is_match(child):
    if 'children' in child:
        for child_market in child['children']:
            if 'marketType' in child_market and child_market['marketType'] == "MATCH_ODDS":
                return True
