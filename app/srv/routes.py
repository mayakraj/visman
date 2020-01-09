from flask import Blueprint, jsonify
from app.db_config.dbManager import as dbm
from app import config_parser
import logging
import psycopg2



queries = config_parser.config(filename='db_config/database.ini', section='queries')

api = Blueprint('srv', __name__)


@api.route('/society_info', methods=['GET', 'POST'])
def society_info():
    """ Gives the society id and society name for all registered society."""
    try:
        query = queries['society_info']

        with dbm.dbManager() as manager:
            result = manager.getDataFrame(query)
            logging.info(result)
            logging.info(result.to_dict(orient='records'))
        return jsonify(result.to_dict(orient='records'))

    except psycopg2.DatabaseError as error:
        errors = {'society info': False, 'error': error}
        return str(errors)