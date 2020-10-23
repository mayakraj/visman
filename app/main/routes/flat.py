from flask_restful import Resource,marshal_with,abort,marshal
from ..models.Flat import Flat
from ..util.decorator import token_required
from ..util.dto import flat_put_args,flat_fields,flat_get_args
from ..service.flat_service import save_flat,get_a_flat


class FlatApi(Resource):
    @marshal_with(flat_fields)
    # @token_required
    def get(self):
        """get a flat id given its args"""
        args = flat_get_args.parse_args()
        flat = get_a_flat(args)
        if not flat:
            abort(404, message="No flat number {} associated with society id {}.".format(
                args['flat_no'],args['society_id']))
        else:
            # return marshal(user,user_fields)
            return flat

    @marshal_with(flat_fields)
    def put(self):
        args = flat_put_args.parse_args()
        return save_flat(data=args)    