import uuid
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import stores
from schemas.schemas import StoreSchema


blp = Blueprint('stores', __name__, description="Operations on Stores.")


@blp.route('/store/<string:id>')
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, id):
        try:
            return stores[id]
        except KeyError:
            abort(404, message="Store not found")

    def delete(self, id):
        try:
            del stores[id]
            return {'message': 'Store deleted successfully!'}, 200
        except KeyError:
            abort(404, message="Store not found")


@blp.route('/store')
class StoreList(MethodView):
    @blp.response(200, StoreSchema)
    def get(self):
        return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):

        for store in stores.values():
            if (store["name"] == store_data["name"]):
                abort(409, message="Store already exists!")

        new_id = uuid.uuid4().hex
        new_store = {**store_data, "id": new_id}
        stores[new_id] = new_store
        return new_store
