from betfair_tennis_api import app, client, cache
from betfair.models import MarketFilter
import requests


@cache.cached(timeout=3600, key_prefix='betfair_navigation')
def get_navigation():
    url = "https://api.betfair.com/exchange/betting/rest/v1/en/navigation/menu.json"
    headers = {
        "Accept": "application/json",
        "X-Application": app.config['BETFAIR_APPLICATION_KEY'],
        "X-Authentication": client.session_token,
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip,deflate"
    }

    app.logger.info("Request made to https://api.betfair.com/exchange/betting/rest/v1/en/navigation/menu.json")
    response = requests.get(url, headers=headers)

    return response.json()


def get_tennis_navigation():
    full_navigation = get_navigation()

    for eventType in full_navigation['children']:
        if eventType['id'] == u'2':
            return eventType

    return "No Tennis :("


def get_tennis_event(event_id):
    market_catalogue = client.list_market_catalogue(
        MarketFilter(event_ids=[event_id])
    )

    return market_catalogue
