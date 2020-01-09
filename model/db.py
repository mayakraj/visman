import logging

from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase
from playhouse.shortcuts import model_to_dict

db = PostgresqlExtDatabase('visman', user='postgres', password='changeme', host='localhost', port='5433')


class BaseModel(Model):

    class Meta:
        database = db
    """Base class for all database models."""

    # exclude these fields from the serialized dict
    EXCLUDE_FIELDS = []

    def serialize(self):
        """Serialize the model into a dict."""
        d = model_to_dict(self, recurse=False, exclude=self.EXCLUDE_FIELDS)
        d["id"] = str(d["id"]) # unification: id is always a string
        return d

    def get_object_or_404(model, **kwargs):
        """Retrieve a single object or abort with 404."""

        try:
            return model.get(**kwargs)
        except model.DoesNotExist:
            logging.warning("NO OBJECT {} {}".format(model, kwargs))
            abort(404)

    def get_object_or_none(model, **kwargs):
        """Retrieve a single object or return None."""

        try:
            return model.get(**kwargs)
        except model.DoesNotExist:
            return None


class User(BaseModel):

    class Meta:
        schema = 'visitor_management_schema'
        db_table = 'user_table'

    id = IdentityField(generate_always=True)
    first_name = CharField()
    middle_name = CharField()
    last_name = CharField()
    username = CharField()
    email = CharField()
    password = CharField()

    def get_user(model,value):
        try:
            if att == 'email':
                return User.select().where(User.email == value).get()

            if att == 'id':
                #return User.select().where(User.id == value).get()
                return BaseModel.get_object_or_404(User, id=value)

        except User.DoesNotExist:
            return 'User does not exist'

    def __str__(self):
        return "Id : {} User Name: {}, email: {} ".format(self.id, self.username, self.email)


class Society(BaseModel):
    id = IdentityField()
    regd_no = CharField()
    name = CharField()
    address = CharField()

    class Meta:
        schema = 'visitor_management_schema'
        db_table = 'society_table'

    # def __init__(self, regdno, name, address, totalBuildings, totalFlats):
    #     self.regdno = regdno
    #     self.name = name
    #     self.address = address
    #     self.totalBuildings = totalBuildings
    #     self.totalFlats = totalFlats

    def get_society_by_regdno(regdno):
        try:
            return Society.select().where(Society.regd_no == regdno).get()
        except User.DoesNotExist:
            return None

    def __str__(self):
        return "Id : {} Society Name: {}, Registration: {}, Addresss: {} ".format(self.id, self.name, self.regd_no, self.address)
