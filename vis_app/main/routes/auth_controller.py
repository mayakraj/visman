from flask import request
from flask_restful import Resource,marshal_with
from app.main.service.auth_helper import Auth
from ..util.dto import user_fields

class LoginAPI(Resource):
    """
         Login Resource
    """
    @marshal_with(user_fields)
    def post(self):
        # get the post data
        post_data = request.form.to_dict()
        return Auth.login_user(data=post_data)

class LogoutAPI(Resource):
    """
    Logout Resource
    """
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
