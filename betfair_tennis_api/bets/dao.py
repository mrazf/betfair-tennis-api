from betfair_tennis_api import client
from betfair import constants


def get_bets():
    bets = []
    cleared_orders = client.list_cleared_orders(constants.BetStatus.SETTLED, [2],
                                                [], [], [], [], None, None, None,
                                                True, None, None, None)['cleared_orders']
    current_orders = client.list_current_orders([2], [], None, None, None, None,
                                                None, None)['current_orders']

    bets.extend(cleared_orders)
    bets.extend(current_orders)

    return bets
