from flask import Flask
from flask_smorest import Api
from blueprints.check import blp as Check_Blueprint
from blueprints.item import blp as Item_Blueprint
from blueprints.store import blp as Store_Blueprint

app = Flask(__name__)

# App and Swagger configs
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = \
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# Registering the app
api = Api(app)

# Registering Blueprints
api.register_blueprint(Check_Blueprint)
api.register_blueprint(Item_Blueprint)
api.register_blueprint(Store_Blueprint)
