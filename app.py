import uuid
from flask import Flask, request
from db import stores, items

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}, 200


@app.post("/store")
def create_store():
    store_data = request.get_json()
    new_id = uuid.uuid4().hex()
    new_store = {**store_data,
                 "id": new_id}
    stores[new_id] = new_store
    return new_store, 201


@app.get("/store/<string:id>")
def get_store_by_id(id):
    try:
        return stores[id], 200
    except KeyError:
        return {'message': 'Store not found'}, 404


@app.get("/item/<string:id>")
def get_item(id):
    try:
        return items[id], 200
    except KeyError:
        return {'message': 'Item not found'}, 404


@app.get("/item")
def get_items():
    return {"items": list(items.values())}, 200


@app.post("/item")
def create_item():
    item_data = request.get_json()

    if (item_data['store_id'] not in stores):
        return {'message': 'ID invalid!'}, 404

    new_id = uuid.uuid4().hex()
    new_item = {**item_data, 'id': new_id}
    items[new_id] = new_item
    return new_item, 201
