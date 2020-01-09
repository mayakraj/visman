from flask import Blueprint, jsonify

api = Blueprint('srv', __name__)


@api.route('/', methods=['GET', 'POST'])
def home():
    """ Returns home page"""
    return "This is the home page."


@api.route('/society_info', methods=['GET', 'POST'])
def society_info():
    """ Gives the society id and society name for all registered society."""
    return "This is for society info"