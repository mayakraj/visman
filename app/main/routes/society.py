
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from app.main.models.Society import Society
from flask import Blueprint
from .. import api, db
from ..util.helper import abort_if_society_id_doesnt_exist

society = Blueprint('society', __name__)

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


resource_fields = {
    'id': fields.Integer,
    'regd_no': fields.String,
    'society_name': fields.String,
    "society_address": fields.String,
    'total_buildings': fields.Integer,
    'total_flats': fields.Integer
}

#custom func
@society.route('/up',methods=['GET'])
def func():
    return 'hello'



class SocietyApi(Resource):
    @marshal_with(resource_fields)
    def get(self, soc_id=None):
        if soc_id is not None:
            result = Society.query.filter_by(id=soc_id).first()
        else:
            result = Society.query.order_by(Society.id).all()
        if not result:
            abort(404, message="No society available")
        return result

    @marshal_with(resource_fields)
    def put(self):
        args = society_put_args.parse_args()
        result = Society.query.filter_by(regd_no=args.regd_no).first()
        if result:
            abort(409, message="society register number already taken...")

        society = Society(**args)
        db.session.add(society)
        db.session.commit()
        return society, 201

    @marshal_with(resource_fields)
    def patch(self):
        args = society_update_args.parse_args()

        result = Society.query.filter_by(id=args.id).first()

        if not result:
            abort(404, message="Society doesn't exist, cannot update")

        if args['regd_no']:
            result.regd_no = args['regd_no']
        if args['society_name']:
            result.society_name = args['society_name']
        if args['society_address']:
            result.society_address = args['society_address']
        db.session.commit()

        return result
    
    
    def delete(self, soc_id):
        abort_if_society_id_doesnt_exist(soc_id)

        result = Society.query.filter_by(id=soc_id).delete()
        db.session.commit()

        return '', 204
