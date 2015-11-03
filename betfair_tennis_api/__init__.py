from flask import Flask
from betfair import Betfair
from betfair.utils import BetfairEncoder

DEBUG = True

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(__name__)
app.config.from_pyfile('config.py')
app.json_encoder = BetfairEncoder

client = Betfair(app.config['BETFAIR_APPLICATION_KEY'], './certs/betfair.pem')
client.login(app.config['BETFAIR_USER_NAME'], app.config['BETFAIR_PASSWORD'])

import betfair_tennis_api.views
