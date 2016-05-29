from betfair_tennis_api import client

def get_current_orders():
    current_orders = client.list_current_orders()['current_orders']

    return [current_order['market_id'] for current_order in current_orders]
