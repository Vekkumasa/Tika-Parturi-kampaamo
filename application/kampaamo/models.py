from application import db
from application.models import Base
from sqlalchemy.sql import text

class Aika(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    pvm = db.Column(db.Date)
    aika_h = db.Column(db.Integer)
    aika_min = db.Column(db.Integer)
    kampaaja_id = db.Column(db.Integer, db.ForeignKey('Kampaaja.id'), nullable=False)

    def __init__(self, pvm, aika_h, aika_min, kampaaja_id):
        self.pvm = pvm
        self.aika_h = aika_h
        self.aika_min = aika_min
        self.kampaaja_id = kampaaja_id

    @staticmethod
    def find_available_times():
        stmt = text("SELECT Aika.id, Aika.pvm FROM Aika, Kampaaja"
                    " WHERE Kampaaja.id = Aika.kampaaja_id")
                    
                    
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "pvm":row[1]})

        return response

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

    varaus_pvm = db.Column(db.Date)

    kampaaja_id = db.Column(db.Integer, db.ForeignKey('Kampaaja.id'), nullable=False)
    asiakas_id = db.Column(db.Integer, db.ForeignKey('asiakas.phoneNumber'), nullable=False)
