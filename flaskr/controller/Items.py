from flask_restful import Resource
from flaskr.repository.database import Database
from flaskr.repository.types.Item import Item


class Items(Resource):

    def get(self, name=None):
        db = Database.get_db()

        items = []
        if name:
            items = db.query(Item).filter_by(name=name).all()
        else:
            items = db.query(Item).all()

        return [item.serialized for item in items]
