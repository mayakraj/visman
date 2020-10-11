
from .. import db
from .. import bcrypt
import datetime
# from app.main.models.blacklist import BlacklistToken
from app.main.models.Flat import Flat
from app.main.models.Society import Society

from ..config import key
import jwt
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    
    __tablename__ = 'user_table'
    __table_args__ = {'schema': 'visitor_management_schema'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # society_id = db.relationship(Society, backref = 'user_table')
    flat_id = db.Column(db.Integer, nullable=False)
    society_id = db.Column(db.Integer, nullable=False)
    # flat_id = db.relationship(Flat, backref='flat_details')
    isadmin = db.Column(db.String(50), nullable=False)
    email_confirmed = db.Column(db.Boolean, nullable=True, default=False)
    user_entity = db.Column(db.Integer,nullable=False)
    identification_type = db.Column(db.String(50), nullable=True)
    identification_no = db.Column(db.String(50), nullable=True)
    photo = db.Column(db.Text(), nullable=True)
    
    def hash_password(self):
       self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
       return check_password_hash(self.password, password)


    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }

            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e    

    @staticmethod
    def decode_auth_token(auth_token):
        """
                Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            # is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            # if is_blacklisted_token:
            #     return 'Token blacklisted. Please log in again.'
            # else:
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return "<User '{}'>".format(self.email)
