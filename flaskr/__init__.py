# flask
from flask import Flask
from flask_restful import Api


def create_app():
    # init flaskr
    app = Flask(__name__)

    # register cli commands
    from .repository.database import Database
    app.cli.add_command(Database.init_db, "init-db")

    # init api
    api = Api(app)

    from .repository.database import Database
    app.teardown_appcontext(Database.close_db)

    from .controller.Root import Root
    from .controller.Items import Items

    api.add_resource(Root, '/')
    api.add_resource(Items, '/items')
    api.add_resource(Items.FilterName, '/items/name/<name>')
    api.add_resource(Items.Delete, '/items/name/<name>/delete')
    api.add_resource(Items.FilterQuality, '/items/quality/<int:quality>')
    api.add_resource(Items.FilterSellIn, '/items/sell_in/<int:sell_in>')
    api.add_resource(Items.UpdateQuality, '/update_quality')

    return app
