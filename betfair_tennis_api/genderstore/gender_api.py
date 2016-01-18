from flask import Flask, Blueprint
from flask_restful import Resource, Api

app = Flask(__name__)
gender_bp = Blueprint('gender_api', __name__, url_prefix="/api/genderStore")
api = Api(gender_bp)


class Player(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(Player, '/player')
