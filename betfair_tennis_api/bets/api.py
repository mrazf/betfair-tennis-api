from flask import Blueprint, jsonify, request
import dao

api = Blueprint('bets_api', __name__, url_prefix='/api')


@api.route('/bets')
def bets():
    bets = dao.get_bets()

    return jsonify(bets=bets)
