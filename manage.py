"""
Created by Charles F. Hayes
Date Created: Feb 12, 2021
No rights reserved. Use as you wish.
"""

from flask.cli import FlaskGroup

from src import create_app, db
from src.api.models import User
from src.api.models import Weight

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()