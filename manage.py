"""
Created by Charles F. Hayes
Date Created: Feb 12, 2021
No rights reserved. Use as you wish.
"""
from flask.cli import FlaskGroup

from src import app


cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()
