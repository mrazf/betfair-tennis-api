from betfair import Betfair
from betfair import constants
from betfair.models import MarketFilter
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamo = boto3.resource('dynamodb', region_name='eu-west-1')
table = dynamo.Table('Player')

print table.scan()
