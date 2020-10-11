import uuid
import datetime

from app.main import db
from app.main.models.User import User
from ..util.helper import abort_if_society_id_doesnt_exist
from flask_restful import abort
from ..util.decorator import CustResponseSend

def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    
    if not user:
        new_user = User(**data)
        new_user.username = data.email 
        new_user.hash_password()
        print(new_user)
        save_changes(new_user)
        return (new_user)
    else:
        abort(404, message="User with email {} alreadey exist".format(data.email))

def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(id=public_id).first()


def generate_token(user):
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)

        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object
        # return auth_token.decode(), 201
    except Exception as e:
      
        return e, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()

