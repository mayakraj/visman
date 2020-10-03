
from flask_restful import reqparse,fields

user_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'username': fields.String,
    "first_name": fields.String,
    'middle_name': fields.String,
    'last_name': fields.String,
    'password': fields.String,
    'society_id': fields.Integer,
    'flat_id': fields.Integer,
    'isadmin': fields.String,
    'email_confirmed': fields.Boolean,
    'user_entity': fields.Integer,
    'identification_type': fields.String,
    'identification_no': fields.String,
    'photo': fields.String
}

user_put_args = reqparse.RequestParser()
user_update_args = reqparse.RequestParser()
user_get_args = reqparse.RequestParser()


user_put_args.add_argument(
    "email", type=str, help="email of the user is required", required=True)
user_put_args.add_argument(
    "first_name", type=str, help="first_name of the user is required", required=True)
user_put_args.add_argument(
    "middle_name", type=str, help="middle_name of the user", required=False)
user_put_args.add_argument(
    "last_name", type=str, help="last_name of the user is required", required=True)
user_put_args.add_argument(
    "password", type=str, help="password of the user is required", required=True)
user_put_args.add_argument(
    "society_id", type=int, help="society_id of the user is required", required=True)
user_put_args.add_argument(
    "flat_id", type=int, help="flat_id of the user is required", required=True)
user_put_args.add_argument(
    "isadmin", type=str, help="isadmin of the user is required", required=True)
user_put_args.add_argument(
    "user_entity", type=int, help="user_entity of the user is required", required=True)
user_put_args.add_argument(
    "identification_type", type=str, help="identification_type in the user", required=False)
user_put_args.add_argument(
    "identification_no", type=str, help="identification_no the user", required=False)           
user_put_args.add_argument(
    "photo", type=str, help="photo of user", required=False)



user_update_args.add_argument(
    "id", type=str, help="id of the user is required", required=True)
user_update_args.add_argument(
    "email", type=str, help="email of the user is required", required=True)
user_update_args.add_argument(
    "username", type=str, help="username of the user is required", required=True)
user_update_args.add_argument(
    "first_name", type=str, help="first_name of the user is required", required=True)
user_update_args.add_argument(
    "middle_name", type=int, help="middle_name of the user", required=False)
user_update_args.add_argument(
    "last_name", type=int, help="last_name of the user is required", required=True)
user_update_args.add_argument(
    "password", type=int, help="password of the user is required", required=True)
user_update_args.add_argument(
    "society_id", type=int, help="society_id of the user is required", required=True)
user_update_args.add_argument(
    "flat_id", type=int, help="flat_id of the user is required", required=True)
user_update_args.add_argument(
    "isadmin", type=int, help="isadmin of the user is required", required=True)
user_update_args.add_argument(
    "user_entity", type=int, help="user_entity of the user is required", required=True)
user_update_args.add_argument(
    "email_confirmed", type=int, help="email_confirmed of user is required", required=False)      
user_update_args.add_argument(
    "identification_type", type=int, help="identification_type in the user", required=True)
user_update_args.add_argument(
    "identification_no", type=int, help="identification_no the user", required=True)           
user_update_args.add_argument(
    "photo", type=int, help="photo of user", required=True)   


user_get_args.add_argument(
    "id", type=int, help="id of the user is required", required=True)    