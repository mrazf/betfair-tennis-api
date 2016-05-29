from flask import Blueprint, jsonify, request
from ..dao import site_navigation
import enrich
import prune_path

matches_api = Blueprint('matches_api', __name__, url_prefix='/api')


@matches_api.route('/matches')
def matches():
    raw_match_paths = site_navigation.get_raw_match_paths()
    enriched_matches = enrich.do(raw_match_paths)
    pruned_matches = prune_path.do(enriched_matches)
    filtered_matches = _filter(pruned_matches)

    result = {
        'matches': filtered_matches,
        'meta': {
            'matchCount': len(raw_match_paths),
            'filteredMatchCount': len(filtered_matches)
        }
    }

    return jsonify(result)


def _filter(matches):
    mens = request.args.get('mens')
    if mens:
        mens = req_bool_conversion(mens)
        matches = filter(lambda m: m['mens'] == mens, matches)

    singles = request.args.get('singles')
    if singles:
        singles = req_bool_conversion(singles)
        matches = filter(lambda m: m['singles'] == singles, matches)

    return matches


def req_bool_conversion(string):
    if string == "true":
        return True
    return False
