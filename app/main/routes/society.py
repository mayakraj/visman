
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from app.main.models.Society import Society
from flask import Blueprint
from .. import api, db
from ..util.helper import abort_if_society_id_doesnt_exist
from ..util.decorator import token_required
from ..util.dto import society_put_args,society_update_args,soc_fields

society = Blueprint('society', __name__)


#custom func
@society.route('/up',methods=['GET'])
def func():
    return 'hello'

class SocietyApi(Resource):
    @marshal_with(soc_fields)
    @token_required
    def get(self, soc_id=None):
        if soc_id is not None:
            result = Society.query.filter_by(id=soc_id).first()
        else:
            result = Society.query.order_by(Society.id).all()
        if not result:
            abort(404, message="No society available")
        return result

    @marshal_with(soc_fields)
    @token_required
    def put(self):
        args = society_put_args.parse_args()
        result = Society.query.filter_by(regd_no=args.regd_no).first()
        if result:
            abort(409, message="society register number already taken...")

        society = Society(**args)
        db.session.add(society)
        db.session.commit()
        return society, 201

    @marshal_with(soc_fields)
    @token_required
    def patch(self):
        args = society_update_args.parse_args()

        result = Society.query.filter_by(id=args.id).first()

        if not result:
            abort(404, message="Society doesn't exist, cannot update")

        for update_key in args.keys():
            if args[update_key]:
                setattr(result, update_key, args[update_key])
        db.session.commit()

        return result
    
    
    def delete(self, soc_id):
        abort_if_society_id_doesnt_exist(soc_id)

        result = Society.query.filter_by(id=soc_id).delete()
        db.session.commit()

        return '', 204
