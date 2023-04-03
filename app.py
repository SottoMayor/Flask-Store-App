from flask import Flask, request
from random import randint

app = Flask(__name__)

stores = [
    {
        "name": "David Store",
        "id": (randint(1, 10) * 100 * randint(1, 10)),
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
