from functools import wraps

from flask import request
from flask_restful import abort

from app.main.service.auth_helper import Auth
import logging

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data = Auth.get_logged_in_user(request)
        token = data.get('user')
        status = data.get('status')
        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated

def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('user')

        if not token:
            return data, status

        admin = token.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated

def fix_null_marshalling(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return _stripNone(result)

    return wrapper   


def require_api_token(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        # Check to see if it's in their session
        if 'api_session_token' not in session:
            # If it isn't return our access denied message (you can also return a redirect or render_template)
            return abort(401,message="Access denied")

        # Otherwise just send them where they wanted to go
        return func(*args, **kwargs)

    return check_token    



def _stripNone(data):
    if isinstance(data, dict):
        return {k: _stripNone(v) for k, v in data.items() if k is not None and v is not None and k is not 0 and v is not 0}
    elif isinstance(data, list):
        return [_stripNone(item) for item in data if item is not None]
    elif isinstance(data, tuple):
        return tuple(_stripNone(item) for item in data if item is not None)
    elif isinstance(data, set):
        return {_stripNone(item) for item in data if item is not None}
    else:
        return data

def CustResponseSend(message, status, outParams):
    logging.debug("In function send")
    print(status, message, outParams)
    response = {"Message": message, "Status": status, "Result": outParams}
    return response    
