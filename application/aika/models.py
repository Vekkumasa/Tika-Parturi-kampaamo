from application import db
from application.models import Base
from sqlalchemy.sql import text

class Aika(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    pvm = db.Column(db.Date)
    aika_h = db.Column(db.Integer)
    aika_min = db.Column(db.Integer)
    vapaa = db.Column(db.Boolean, nullable=False)

    kampaaja_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    varaus = db.relationship("Varaus", backref="Aika", lazy=True)

    def __init__(self, pvm, aika_h, aika_min, kampaaja_id):
        self.pvm = pvm
        self.aika_h = aika_h
        self.aika_min = aika_min
        self.kampaaja_id = kampaaja_id
        self.vapaa = True