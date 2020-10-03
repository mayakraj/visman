from flask import request
from flask_restful import Resource,marshal_with,abort
from app.main.util.decorator import admin_token_required
from ..util.dto import user_fields,user_put_args,user_update_args,user_get_args
from ..service.user_service import save_new_user, get_all_users, get_a_user
from ...main.util.decorator import CustResponseSend


class UserListApi(Resource):
    @marshal_with(user_fields)
    # @admin_token_required
    def get(self):
        """List all registered users"""
        return get_all_users()

    def put(self):
        """Creates a new User """
        args = user_put_args.parse_args()
        args['email_confirmed'] = False
        return save_new_user(data=args)

class UserApi(Resource):
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            return CustResponseSend('No user with this id available.',True,[])
            # abort(404, message="No user with this id available")
        else:
            return user

