from flask import Blueprint, jsonify
from app.db_config.dbManager import as dbm
from app import config_parser
import logging
import psycopg2



queries = config_parser.config(filename='db_config/database.ini', section='queries')

api = Blueprint('srv', __name__)


@api.route('/', methods=['GET', 'POST'])
def home():
    """ Returns home page"""
    return "This is the home page."

@api.route('/society_info', methods=['GET', 'POST'])
def society_info():
    """ Gives the society id and society name for all registered society."""
    return "This is for society info"