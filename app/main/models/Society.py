from .. import db


class Society(db.Model):

    __tablename__ = 'society_table'
    __table_args__ = {'schema': 'visitor_management_schema'}
    id = db.Column(db.Integer,primary_key=True)
    regd_no=db.Column(db.String(1000),nullable=False)
    society_name = db.Column(db.String(1000), nullable=False)
    society_address = db.Column(db.String(1000), nullable=False)
    total_buildings = db.Column(db.Integer)
    total_flats = db.Column(db.Integer)
    # flat_details = db.relationship("Flat")


    # def serialize(self):
    #     """Serialize this object to dict/json."""
    #     d = super(Society, self).serialize()
    #     return d

    # def __str__(self):
    #     return "Id : {} Society Name: {}, RegdNo: {}, Address:{}, Total Buildings: {}, Total Flats: {}".format(self.id, self.society_name,
    #      self.regd_no, self.society_address, self.total_buildings, self.total_flats)
    def __repr__(self):
        return "<Society '{}'>".format(self.society_name)
