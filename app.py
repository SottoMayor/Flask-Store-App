from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "David Store",
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


@app.route("/stores")
def get_stores():
    return {'stores': stores}
