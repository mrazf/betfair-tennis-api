from flask import Blueprint, jsonify
import boto3
from boto3.dynamodb.conditions import Key, Attr

player_bp = Blueprint('player_api', __name__, url_prefix="/api")
dynamo = boto3.resource('dynamodb', region_name='eu-west-1')

@player_bp.route('/player/<name>')
def player(name):
    table = dynamo.Table('Player')

    return jsonify(table.get_item(Key={'BetfairName': name}))
