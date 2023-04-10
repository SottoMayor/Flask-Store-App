import uuid
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import items
from schemas.schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint('item', __name__, description="Operations on Items")


@blp.route("/item/<string:id>")
class Item(MethodView):

    @blp.response(200, ItemSchema)
    def get(self, id):
        try:
            return items[id], 200
        except KeyError:
            abort(404, message="Item not found")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, id):

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

    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):

        for item in items.values():
            if (item["name"] == item_data["name"] and
                    item["item_id"] == item_data["item_id"]):
                abort(409, message="Item already exists!")

        if (item_data['item_id'] not in items):
            abort(404, message="ID Invalid!!")

        new_id = uuid.uuid4().hex
        new_item = {**item_data, 'id': new_id}
        items[new_id] = new_item
        return new_item
