from application import db
from application.models import Base

class Kampaaja(Base):

    varaukset = db.relationship("Varaus", backref='Kampaaja', lazy=True)

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

class Asiakas(Base):

    phoneNumber = db.Column(db.String(144))
    varaukset = db.relationship("Varaus", backref='Asiakas', lazy=True)

    def __init__(self, firstName, lastName, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber

class Varaus(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                    onupdate=db.func.current_timestamp())

    varattu_aika = db.Column(db.DateTime, default=db.func.current_timestamp(),
                    onupdate=db.func.current_timestamp())

    kampaaja_id = db.Column(db.Integer, db.ForeignKey('kampaaja.id'), nullable=False)
    asiakas_id = db.Column(db.Integer, db.ForeignKey('asiakas.id'), nullable=False)
