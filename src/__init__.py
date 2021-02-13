# -*- coding: utf-8 -*-
# pylint: disable=no-member
"""
Created by Charles F. Hayes
Date Created: Feb 12, 2021
No rights reserved. Use as you wish.
"""
import os
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy


# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class Weight(db.Model):
    __tablename__ = 'weight'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    weight = db.Column(db.Float(3,1), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, username, weight, date):
        self.username = username
        self.weight = weight
        self.date = date


class Health(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'service is running!'
        }


db.create_all()
db.session.commit()

api.add_resource(Health, '/health')