db = PostgresqlExtDatabase('d5267ba9erjt2u', user='gawsmrxbzfvrmf', password='4e011cd366dd047014b1e42fa8992a6e4eeabc164f21053a37435a8b5ee4b289', host='ec2-54-227-251-33.compute-1.amazonaws.com', port='5432')


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
