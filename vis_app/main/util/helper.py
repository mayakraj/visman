from flask_restful import abort
from app.main.models.Society import Society


def abort_if_society_id_doesnt_exist(society_id):
    result = Society.query.filter_by(id=society_id).first()
    print(result)
    if not result:
        abort(404, message='No society present for this id')
