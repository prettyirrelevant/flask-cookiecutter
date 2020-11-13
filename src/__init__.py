from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from . import cli

db = SQLAlchemy()
migrate = Migrate()


def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    # Additional config can be added here

    db.init_app(app)
    migrate.init_app(app, db)

    app.cli.add_command(cli.blueprints_cli)

    with app.app_context():
        from . import routes

        # Blueprints registration goes here!

        return app
