from flask import jsonify
from betfair_tennis_api import app
from dao import site_navigation
import matches
import match_path


@app.route("/betfair-tennis-api/tennisNavigation/")
def tennis_navigation():
    return jsonify(site_navigation.get_tennis_navigation())


@app.route("/betfair-tennis-api/tennisMatches/")
def tennis_matches():
    return jsonify(tennisMatches=matches.get_tennis_matches())


@app.route("/betfair-tennis-api/tennisMatches/<event_id>/")
def tennis_match(event_id):
    events = site_navigation.get_tennis_event(event_id)

    return jsonify(market_catalogue=events)


@app.route("/betfair-tennis-api/rawMatchPaths")
def _match_path():
    tennis_matches = site_navigation.get_tennis_navigation()

    return jsonify(rawMatchPaths=match_path.get(tennis_matches))
