from ..models.Flat import Flat
from ..models.Society import Society

from ..util.helper import save_changes


def save_flat(data):
    #to check society exist or not
    #society =  Society.query.filter(society_id=society_id).first()
    
    flat = Flat.query.filter_by(flat_no=data['flat_no'],society_id=data['society_id'],wing=data['wing']).first() 

    if not flat:
        new_flat = Flat(**data)
        print(new_flat)
        save_changes(new_flat)

        return new_flat

def get_a_flat(data):
    return Flat.query.filter_by(society_id=data['society_id'],flat_no=data['flat_no'],wing=data['wing']).first()  

