from flask import Flask
from flask.ext.cache import Cache
from betfair import Betfair
from betfair.utils import BetfairEncoder
from cStringIO import StringIO
import os


application = app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('APP_CONFIG_FILE')
app.json_encoder = BetfairEncoder

f = open('betfair.pem', 'w+')
f.write(os.environ['testvar'])
f.close()

client = Betfair(app.config['BETFAIR_APPLICATION_KEY'], 'betfair.pem')
client.login(app.config['BETFAIR_USER_NAME'], app.config['BETFAIR_PASSWORD'])

cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

import betfair_tennis_api.views

if __name__ == "__main__":
    application.run(host='0.0.0.0')
