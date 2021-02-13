from sqlalchemy.sql import func

from src import db


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
    date_created = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username, weight, date_created):
        self.username = username
        self.weight = weight
        self.date_created = date_created
