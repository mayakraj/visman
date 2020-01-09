db = PostgresqlExtDatabase('visman', user='postgres', password='changeme', host='localhost', port='5433')


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
