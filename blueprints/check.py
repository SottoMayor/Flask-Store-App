from flask.views import MethodView
from flask_smorest import Blueprint

blp = Blueprint('check', __name__, description='Check the health of the app.')


@blp.route('/check')
class Check(MethodView):
    def get(self):
        return "<p>Hello, World!</p>"
