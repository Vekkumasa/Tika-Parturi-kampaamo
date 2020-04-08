from application import db
from application.models import Base
from sqlalchemy.sql import text

class Aika(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    pvm = db.Column(db.Date)
    aika_h = db.Column(db.Integer)
    aika_min = db.Column(db.Integer)
    vapaa = db.Column(db.Boolean, nullable=False)

    kampaaja_id = db.Column(db.Integer, db.ForeignKey('Kampaaja.id'), nullable=False)
    varaus = db.relationship("Varaus", backref="Aika", lazy=True)

    def __init__(self, pvm, aika_h, aika_min, kampaaja_id):
        self.pvm = pvm
        self.aika_h = aika_h
        self.aika_min = aika_min
        self.kampaaja_id = kampaaja_id
        self.vapaa = True

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

    kampaaja_id = db.Column(db.Integer, db.ForeignKey('Kampaaja.id'), nullable=False)
    asiakas_id = db.Column(db.Integer, db.ForeignKey('asiakas.phoneNumber'), nullable=False)
    aika_id = db.Column(db.Integer, db.ForeignKey('aika.id'), nullable=False)

    @staticmethod
    def find_reservations(varaus_id):
        stmt = text("SELECT Varaus.id, Aika.id, Aika.pvm, Aika.aika_h, Aika.aika_min, Asiakas.firstName FROM Varaus"
                    " LEFT JOIN Aika On Aika.id = Varaus.aika_id"
                    " LEFT JOIN Asiakas ON Asiakas.phoneNumber = Varaus.asiakas_id "
                    " WHERE Varaus.id = %s" % varaus_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "aika_id":row[1], "aika_pvm":row[2], "aika_h":row[3], "aika_min":row[4], "asiakas_name":row[5]})

        return response
