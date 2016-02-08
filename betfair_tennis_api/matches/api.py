from flask import Blueprint, jsonify
from ..dao import site_navigation
import enrich
import prune_path

api = Blueprint('matches_api', __name__, url_prefix='/api')


@api.route('/matches')
def matches():
    raw_match_paths = site_navigation.get_raw_match_paths()
    enriched_matches = enrich.do(raw_match_paths)
    pruned_matches = prune_path.do(enriched_matches)

    return jsonify(matches=pruned_matches)
