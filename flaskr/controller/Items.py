from flask_restful import Resource
from flask import abort
from flaskr.repository.database import Database
from flaskr.repository.types.Item import Item


class Items:
    class FilterName(Resource):
        def get(self, name=None):
            db = Database.get_db()

            items = []
            if name:
                items = db.query(Item).filter_by(name=name).all()
            else:
                items = db.query(Item).all()

            return [item.serialized for item in items]

    class FilterQuality(Resource):
        def get(self, quality: str = ""):
            if quality.isdigit():
                quality = int(quality)
                db = Database.get_db()
                items = db.query(Item).filter_by(quality=quality).all()
                return [item.serialized for item in items]

            return abort(400, "'quality' should be a number")

    class FilterSellIn(Resource):
        def get(self, sell_in: str = ""):
            if sell_in.isdigit():
                sell_in = int(sell_in)
                db = Database.get_db()
                items = db.query(Item).filter_by(sell_in=sell_in).all()
                return [item.serialized for item in items]

            return abort(400, "'sell_in' should be a number")
