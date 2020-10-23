
from .. import db
import datetime
# from app.main.models.blacklist import BlacklistToken


class Flat(db.Model):
    
    __tablename__ = 'flat_details'
    __table_args__ = {'schema': 'visitor_management_schema'}

    id = db.Column(db.Integer,primary_key=True)
    flat_no = db.Column(db.Integer, nullable=False)
    wing = db.Column(db.String(50), nullable=False)

    society_id = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return "<Flat '{}'>".format(self.flat_no)