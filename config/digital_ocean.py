import os

BETFAIR_APPLICATION_KEY = os.environ['BETFAIR_APPLICATION_KEY']
BETFAIR_USER_NAME = os.environ['BETFAIR_USER_NAME']
BETFAIR_PASSWORD = os.environ['BETFAIR_PASSWORD']

with open('/home/stringer/betfair.pem', 'r') as pem:
    PEM_FILE = pem.read()
