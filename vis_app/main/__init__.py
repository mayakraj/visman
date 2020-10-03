from flask import Flask,Blueprint,make_response,jsonify
from flask import json
from werkzeug.exceptions import HTTPException
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import jwt_manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://azqkdeiqpezmzj:ee1246a50f9c0d67038106e0557c7eddd05bdd0fda2149d831354388f53d70a9@ec2-54-235-250-38.compute-1.amazonaws.com:5432/d3u39l3sta71kl'

db = SQLAlchemy(app)
api = Api(app)

CORS(app)
bcrypt = Bcrypt(app)

# jwt = jwt_manager()


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'URL Not found'}), 404)

from werkzeug.exceptions import HTTPException

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response    



