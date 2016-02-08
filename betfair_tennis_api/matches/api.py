from flask import Blueprint, jsonify
from ..dao import site_navigation
import enrich

api = Blueprint('matches_api', __name__, url_prefix='/api')


@api.route('/matches')
def matches():
    raw_match_paths = site_navigation.get_raw_match_paths()

    return jsonify(matches=enrich.do(raw_match_paths))
