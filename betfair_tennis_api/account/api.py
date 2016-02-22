from flask import Blueprint, jsonify
from betfair import constants
import json
from betfair_tennis_api import client

api = Blueprint('account_api', __name__, url_prefix='/api')
ACCOUNT_KEYS = ['available_to_bet_balance', 'exposure', 'wallet']


@api.route("/account")
def get_account():
    account_funds_resp = client.get_account_funds()
    account_statement = client.get_account_statement(include_item=constants.IncludeItem['EXCHANGE'])
    account = {
        'balance': account_funds_resp['available_to_bet_balance'],
        'exposure': account_funds_resp['exposure'],
        'tennisProfit': get_tennis_profit(account_statement),
        'wallet': account_funds_resp['wallet']
    }

    return jsonify(account)


def get_tennis_profit(account_statement):
    profit = 0.0
    for statement in account_statement.account_statement:
        item_data = json.loads(statement.item_class_data['unknownStatementItem'])

        if item_data['eventTypeId'] is 2:
            profit = profit + statement.amount

    return profit
