import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import items

blp = Blueprint('item', __name__, description="Operations on Items")


@blp.route("/item/<string:id>")
class Item(MethodView):
    def get(self, id):
        try:
            return items[id], 200
        except KeyError:
            abort(404, message="Item not found")

    def put(self, id):
        item_data = request.get_json()

        try:
            item = items[id]
            item |= item_data

            return item
        except KeyError:
            abort(404, message='Trying to update an inexisting item!')

    def delete(self, id):
        try:
            del items[id]
            return {'message': 'Item deleted successfully!'}, 200
        except KeyError:
            abort(404, message="Item not found")


@blp.route("/item")
class ItemList(MethodView):
    def get(self, id):
        return {"items": list(items.values())}, 200

    def post(self, id):
        item_data = request.get_json()

        for item in items.values():
            if (item["name"] == item_data["name"] and
                    item["store_id"] == item_data["store_id"]):
                abort(409, message="Item already exists!")

        if (item_data['store_id'] not in items):
            abort(404, message="ID Invalid!!")

        new_id = uuid.uuid4().hex
        new_item = {**item_data, 'id': new_id}
        items[new_id] = new_item
        return new_item, 201
