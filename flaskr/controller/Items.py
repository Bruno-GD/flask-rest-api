from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from flask import abort, make_response, g
from flaskr.domain.GildedRose import GildedRose
from flaskr.repository.queries import Query


class Items(Resource):
    def __init__(self):
        self.parser = RequestParser()
        self.parser.add_argument("name", type=str, required=True)
        self.parser.add_argument("quality", type=int, required=True)
        self.parser.add_argument("sell_in", type=int, required=True)

    def get(self):
        return Query.get_all()

    def post(self):
        args = self.parser.parse_args()
        if isinstance(args['name'], str) and \
                isinstance(args['quality'], int) and \
                isinstance(args['sell_in'], int):
            item = Query.insert_one(args)
            # devolvemos 202, cuando se cierre el app_context
            # se guardará en la base de datos
            return make_response(item, 202)

        return abort(400)

    class FilterName(Resource):
        def get(self, name: str = None):
            if name:
                return Query.get_all({"name": name})

    class FilterQuality(Resource):
        def get(self, quality: int = None):
            if quality:
                return Query.get_all({"quality": quality})

            return abort(400, "'quality' should be a number")

    class FilterSellIn(Resource):
        def get(self, sell_in: int = None):
            if sell_in:
                return Query.get_all({"sell_in": sell_in})

            return abort(400, "'sell_in' should be a number")

    class UpdateQuality(Resource):
        def get(self):
            if 'shop' not in g:
                items = Query.get_all()
                g.shop = GildedRose(GildedRose.get_items_typeof(items))

            g.shop.update_quality()

            return make_response("Updated", 202)

    class Delete(Resource):

        def delete(self, name: str = None):
            Query.delete_all({"name": name})
            return make_response("Deleted", 202)
