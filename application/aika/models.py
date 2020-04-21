from application import db
from sqlalchemy.sql import text

class Aika(db.Model):

    __tablename__ = "Aika"

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

    @staticmethod
    def vapaat_ajat(kampaaja_id):
        stmt = text("SELECT * FROM Aika WHERE vapaa=1 AND Kampaaja_id = %s" % kampaaja_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "pvm":row[1], "aika_h":row[2], "aika_min":row[3], "vapaa":row[4] })

        return response