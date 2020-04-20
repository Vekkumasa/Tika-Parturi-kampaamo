from application import db
from application.models import Base
from sqlalchemy.sql import text

class Asiakas(Base):

    __tablename__ = "Asiakas"

    phonenumber = db.Column(db.String(144), primary_key=True, nullable=False)
    varaukset = db.relationship("Varaus", backref='Asiakas', lazy=True)

    def __init__(self, firstName, lastName, phonenumber):
        self.firstName = firstName
        self.lastName = lastName
        self.phonenumber = phonenumber