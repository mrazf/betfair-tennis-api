from flask import Blueprint, jsonify
from betfair import constants
import json
from betfair_tennis_api import client

account_api = Blueprint('account_api', __name__, url_prefix='/api')


@account_api.route("/account")
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
    tennis_items = filter(is_tennis_item, account_statement.account_statement)
    profit = reduce(lambda cumulative, item: cumulative + item.amount, tennis_items, 0.0)

    return profit


def is_tennis_item(item):
    item_data = json.loads(item.item_class_data['unknownStatementItem'])

    if 'eventTypeId' in item_data and item_data['eventTypeId'] is 2:
        return True

    return False
