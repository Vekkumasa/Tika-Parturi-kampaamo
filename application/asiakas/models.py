from application import db
from application.models import Base
from sqlalchemy.sql import text

class Asiakas(db.Model):

    __tablename__ = "Asiakas"

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    firstName = db.Column(db.String(144), nullable=False)
    lastName = db.Column(db.String(144), nullable=False)

    phoneNumber = db.Column(db.Integer, primary_key=True, nullable=False)
    varaukset = db.relationship("Varaus", backref='Asiakas', lazy=True)

    def __init__(self, firstName, lastName, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber