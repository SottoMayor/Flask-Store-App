import uuid
from flask import Flask, request
from flask_smorest import abort
from db import stores, items

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# STORES ...


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}, 200


@app.post("/store")
def create_store():
    store_data = request.get_json()

    for store in stores.values():
        if (store["name"] == store_data["name"]):
            abort(409, message="Store already exists!")

    new_id = uuid.uuid4().hex
    new_store = {**store_data,
                 "id": new_id}
    stores[new_id] = new_store
    return new_store, 201


@app.get("/store/<string:id>")
def get_store_by_id(id):
    try:
        return stores[id], 200
    except KeyError:
        abort(404, message="Store not found")


@app.delete("/store/<string:id>")
def delete_store(id):
    try:
        del stores[id]
        return {'message': 'Store deleted successfully!'}, 200
    except KeyError:
        abort(404, message="Store not found")


# ITEMS ...


@app.get("/item/<string:id>")
def get_item(id):
    try:
        return items[id], 200
    except KeyError:
        abort(404, message="Item not found")


@app.get("/item")
def get_items():
    return {"items": list(items.values())}, 200


@app.post("/item")
def create_item():
    item_data = request.get_json()
    print(item_data)

    for item in items.values():
        if (item["name"] == item_data["name"] and
                item["store_id"] == item_data["store_id"]):
            abort(409, message="Item already exists!")

    if (item_data['store_id'] not in stores):
        abort(404, message="ID Invalid!!")

    new_id = uuid.uuid4().hex
    new_item = {**item_data, 'id': new_id}
    items[new_id] = new_item
    return new_item, 201


@app.put('/item/<string:id>')
def update_item(id):
    item_data = request.get_json()

    try:
        item = items[id]
        item |= item_data

        return item
    except KeyError:
        abort(404, message='Trying to update an inexisting item!')


@app.delete("/item/<string:id>")
def delete_item(id):
    try:
        del items[id]
        return {'message': 'Item deleted successfully!'}, 200
    except KeyError:
        abort(404, message="Item not found")
