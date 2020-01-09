from flask import Blueprint, jsonify, request
from app.model import User

api = Blueprint('model', __name__)


@api.route('/getuser', methods=['GET', 'POST'])
def getuser():
    email = request.form[email]
    user = User.get_user(email)
    return jsonify(user)
