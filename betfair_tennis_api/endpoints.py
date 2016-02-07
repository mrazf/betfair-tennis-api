from json import loads as json_loads
from flask import jsonify
from betfair_tennis_api import app
from dao import site_navigation

with open('swagger.json', 'r') as f:
    schema = json_loads(f.read())


@app.route("/api/fullNavigation")
def full_navigation():
    return jsonify(site_navigation.get_navigation())


@app.route("/api/tennisNavigation/")
def tennis_navigation():
    return jsonify(site_navigation.get_tennis_navigation())


@app.route("/api/rawMatchPaths")
def raw_match_paths():
    return jsonify(tennisMatches=site_navigation.get_raw_match_paths())


@app.route("/api/vista")
def schema_definition():
    return jsonify(schema)
