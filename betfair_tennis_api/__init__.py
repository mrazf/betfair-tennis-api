from flask import Flask
from flask.ext.cache import Cache
from flask.ext.cors import CORS
from betfair import Betfair
from betfair.utils import BetfairEncoder
import logging


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('APP_CONFIG_FILE')
app.json_encoder = BetfairEncoder

f = open('./config/betfair.pem', 'w+')
f.write(app.config['PEM_FILE'])
f.close()

client = Betfair(app.config['BETFAIR_APPLICATION_KEY'], './config/betfair.pem')
client.login(app.config['BETFAIR_USER_NAME'], app.config['BETFAIR_PASSWORD'])

cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

CORS(app, origins=['http://localhost:4200'])

stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)

import betfair_tennis_api.endpoints
import enrichment
import account

if __name__ == "__main__":
    app.run(host='0.0.0.0')
