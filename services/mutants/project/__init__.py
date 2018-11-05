import os

from flask import Flask
from flask_pymongo import PyMongo

# instantiate the db
mongo = PyMongo()


def create_app(script_info=None):
    ''' Factory pattern for flask app'''

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # factory init (instantiate) mongo
    mongo.init_app(app, uri=os.environ['MONGO_URI'])

    # register blueprints
    from project.api.mutant_api import mutants_blueprint
    app.register_blueprint(mutants_blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app})
    return app
