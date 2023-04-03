from flask import Flask, request
from random import randint

app = Flask(__name__)

stores = [
    {
        "name": "David Store",
        "id": 1,
        "items": [
            {
                "name": "PC",
                "price": "5000"
            }
        ]
    }
]


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    body = request.get_json()
    new_store = {"name": body["name"], "items": [],
                 "id": (randint(1, 10) * 100 * randint(1, 10))}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<int:id>/item")
def create_item(id):
    body = request.get_json()
    new_item = {"name": body["name"], "price": body["price"]}

    for index, store in enumerate(stores):
        if(store['id'] == id):
            stores[index]['items'].append(new_item)
            return new_item, 201
    return {'message': 'ID invalid!'}, 404
