from flask import Blueprint, jsonify

player_bp = Blueprint('player_api', __name__, url_prefix="/api")

@player_bp.route('/player/<id>')
def player(id):
    return jsonify(player=id)
