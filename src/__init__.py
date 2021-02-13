"""
Created by Charles F. Hayes
Date Created: Feb 12, 2021
No rights reserved. Use as you wish.
"""
from flask import Flask, jsonify
from flask_restx import Resource, Api


# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app.config.from_object('src.config.DevelopmentConfig')


class Health(Resource):
    """
    The Health resource is used for checking the health of this microservice
    """
    def get(self):
        """
        Returns a success message if this service is running.
        """
        return {
            'status': 'success',
            'message': 'The service is running!'
        }


api.add_resource(Health, '/health')
