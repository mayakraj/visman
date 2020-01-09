from playhouse.db_url import connect

#from playhouse import PostgresqlExtDatabase

db = connect('postgres://azqkdeiqpezmzj:ee1246a50f9c0d67038106e0557c7eddd05bdd0fda2149d831354388f53d70a9@ec2-54-235-250-38.compute-1.amazonaws.com:5432/d3u39l3sta71kl')


class BaseModel(Model):

    class Meta:
        database = db


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

    def get_user(self, value):
        try:
            if att == 'email':
                return User.select().where(User.email == value).get()

            if att == 'id':
                return User.select().where(User.id == value).get()
                #return BaseModel.get_object_or_404(User, id=value)

        except User.DoesNotExist:
            return 'User does not exist'

    def __str__(self):
        return "Id : {} User Name: {}, email: {} ".format(self.id, self.username, self.email)
