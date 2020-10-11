from flask import request
from flask_restful import Resource,marshal_with,abort
from ..util.dto import user_fields,user_put_args,user_update_args,user_get_args
from ..service.user_service import save_new_user, get_all_users, get_a_user
from ...main.util.decorator import CustResponseSend,fix_null_marshalling
from app.main.util.decorator import token_required

class UserListApi(Resource):
    @marshal_with(user_fields)
    @token_required
    def get(self):
        """List all registered users"""
        return get_all_users()
    
    @marshal_with(user_fields)
    @token_required
    def put(self):
        """Creates a new User """
        args = user_put_args.parse_args()
        args['email_confirmed'] = False
        return save_new_user(data=args)

class UserApi(Resource):
    @marshal_with(user_fields)
    @token_required
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            abort(404, message="No user with this id available")
        else:
            return user