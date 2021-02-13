from flask import Blueprint
from flask_restx import Resource, Api


health_blueprint = Blueprint('health', __name__)
api = Api(health_blueprint)


class Health(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'service is running!'
        }


api.add_resource(Health, '/health')