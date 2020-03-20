from application import db
from application.models import Base

class Asiakas(Base):

    phoneNumber = db.Column(db.String(144), primary_key=True, nullable=False)
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

    kampaaja_id = db.Column(db.Integer, db.ForeignKey('Kampaaja.id'), nullable=False)
    asiakas_id = db.Column(db.Integer, db.ForeignKey('asiakas.phoneNumber'), nullable=False)
