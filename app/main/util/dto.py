
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
    "id", type=str, help="id of the user is required", required=False)
user_update_args.add_argument(
    "email", type=str, help="email of the user is required", required=False)
user_update_args.add_argument(
    "username", type=str, help="username of the user is required", required=False)
user_update_args.add_argument(
    "first_name", type=str, help="first_name of the user is required", required=False)
user_update_args.add_argument(
    "middle_name", type=str, help="middle_name of the user", required=False)
user_update_args.add_argument(
    "last_name", type=str, help="last_name of the user is required", required=False)
user_update_args.add_argument(
    "password", type=str, help="password of the user is required", required=False)
user_update_args.add_argument(
    "society_id", type=int, help="society_id of the user is required", required=False)
user_update_args.add_argument(
    "flat_id", type=int, help="flat_id of the user is required", required=False)
user_update_args.add_argument(
    "isadmin", type=bool, help="isadmin of the user is required", required=False)
user_update_args.add_argument(
    "user_entity", type=int, help="user_entity of the user is required", required=False)
user_update_args.add_argument(
    "email_confirmed", type=bool, help="email_confirmed of user is required", required=False)      
user_update_args.add_argument(
    "identification_type", type=str, help="identification_type in the user", required=False)
user_update_args.add_argument(
    "identification_no", type=str, help="identification_no the user", required=False)           
user_update_args.add_argument(
    "photo", type=str, help="photo of user", required=False)   


user_get_args.add_argument(
    "id", type=int, help="id of the user is required", required=True)    




society_put_args = reqparse.RequestParser()
society_put_args.add_argument(
    "regd_no", type=str, help="Registered number of the society is required", required=True)
society_put_args.add_argument(
    "society_name", type=str, help="Name of the society is required", required=True)
society_put_args.add_argument(
    "society_address", type=str, help="Address of the society", required=True)
society_put_args.add_argument(
    "total_buildings", type=int, help="total buildings in the society", required=True)
society_put_args.add_argument(
    "total_flats", type=int, help="total flats in the society", required=True)

society_update_args = reqparse.RequestParser()
society_update_args.add_argument(
    "id", type=int, help="id of the society is required", required=True)
society_update_args.add_argument(
    "regd_no", type=str, help="Registered number of the society is required", required=False)
society_update_args.add_argument(
    "society_name", type=str, help="Name of the society is required", required=False)
society_update_args.add_argument(
    "society_address", type=str, help="Address of the society", required=False)
society_update_args.add_argument(
    "total_buildings", type=int, help="total buildings in the society", required=False)
society_update_args.add_argument(
    "total_flats", type=int, help="total flats in the society", required=False)


soc_fields = {
    'id': fields.Integer,
    'regd_no': fields.String,
    'society_name': fields.String,
    "society_address": fields.String,
    'total_buildings': fields.Integer,
    'total_flats': fields.Integer
}