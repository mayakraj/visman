from flask import request
from flask_restful import Resource,marshal_with,abort,marshal
from .. import  db
from app.main.models.User import User
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

    @marshal_with(user_fields)
    @token_required
    def patch(self):
        args = user_update_args.parse_args()
        result = get_a_user(args.id)

        if not result:
            abort(404, message="User doesn't exist, cannot update")

        for update_key in args.keys():
            if args[update_key]:
                setattr(result, update_key, args[update_key])
            
        db.session.commit()

        return result     

class UserApi(Resource):
    @marshal_with(user_fields)
    @token_required
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            abort(404, message="No user with this id available")
        else:
            # return marshal(user,user_fields)
            return user

            

           
            