# flask
from flask import Flask
from flask_restful import Api


def create_app():
    # init flaskr
    app = Flask(__name__)
    api = Api(app)

    from .repository.database import Database
    app.teardown_appcontext(Database.close_db)

    from .controller.Root import Root
    from .controller.Items import Items

    api.add_resource(Root, '/')
    api.add_resource(Items, '/items', '/items/<name>')

    return app
