from application import db
from application.models import Base
from sqlalchemy.sql import text

class Varaus(db.Model):

    __tablename__ = "Varaus"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                    onupdate=db.func.current_timestamp())

    kampaaja_id = db.Column(db.Integer, db.ForeignKey('Kampaaja.id'), nullable=False)
    asiakas_id = db.Column(db.Integer, db.ForeignKey('Asiakas.phoneNumber'), nullable=False)
    aika_id = db.Column(db.Integer, db.ForeignKey('Aika.id'), nullable=False)

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