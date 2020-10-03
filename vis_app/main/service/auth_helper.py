from app.main.models.User import User
from ..service.blacklist_service import save_token
from flask_restful import abort
from flask import jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta
# from ..util.decorator import CustResponseSend

class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data['username']).first()
            if user and user.check_password(data['password']):
                expires = timedelta(days=7)
                print('IN LOGIN______________________')
                token = create_access_token(identity=str(user.id), expires_delta=expires)
                response = {'Message':'Login successful','Status':True,'Result':{'token':token,'user':user}}
                return jsonify(response)
            else:
                abort(400,message='User login credentials doesn\'t match')    

        except Exception as e:
            abort(500,message=e)

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': user
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
