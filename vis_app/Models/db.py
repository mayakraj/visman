import os
from playhouse.db_url import connect

# DATABASE_URL = os.environ['DATABASE_URL']

#DATABASE_URL = 'postgresql://postgres:changeme@localhost:5432/visman'

# visman test database url
DATABASE_URL = 'postgres://gawsmrxbzfvrmf:4e011cd366dd047014b1e42fa8992a6e4eeabc164f21053a37435a8b5ee4b289@ec2-54-227-251-33.compute-1.amazonaws.com:5432/d5267ba9erjt2u'


def db_connect():
    try:
        db = connect(DATABASE_URL, autorollback=True)
        return db

    except Exception as error:
        return str(error)
