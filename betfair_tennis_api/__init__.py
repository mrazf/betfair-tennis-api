from flask import Flask
from flask.ext.cache import Cache
from flask.ext.cors import CORS
from betfair import Betfair
from betfair.utils import BetfairEncoder
import logging

app = application = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('BETFAIR_API_CONFIG')
app.json_encoder = BetfairEncoder

client = Betfair(app.config['BETFAIR_APPLICATION_KEY'], app.config['BETFAIR_PEM_PATH'])
client.login(app.config['BETFAIR_USER_NAME'], app.config['BETFAIR_PASSWORD'])

cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

CORS(app, origins=['http://localhost:4200', 'http://stringerer.s3-website-eu-west-1.amazonaws.com'])

stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)

import betfair_tennis_api.endpoints
from betfair_tennis_api.matches import matches_api
from betfair_tennis_api.account import account_api
app.register_blueprint(matches_api)
app.register_blueprint(account_api)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
