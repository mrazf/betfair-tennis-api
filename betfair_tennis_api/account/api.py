from flask import Blueprint, jsonify
from betfair_tennis_api import client

api = Blueprint('account_api', __name__, url_prefix='/api')
ACCOUNT_KEYS = ['available_to_bet_balance', 'exposure', 'wallet']


@api.route("/account")
def get_account():
    account_funds_resp = client.get_account_funds()
    account = {req_key: account_funds_resp[req_key] for req_key in ACCOUNT_KEYS}

    return jsonify(account)
