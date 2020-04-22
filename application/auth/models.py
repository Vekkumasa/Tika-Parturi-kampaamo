from application import db
from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "Kampaaja"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                    onupdate=db.func.current_timestamp())
    
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    varaukset = db.relationship("Varaus", backref='Kampaaja', lazy=True)
    vapaat_ajat = db.relationship("Aika", backref='Kampaaja', lazy=True)
    

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN"]

    @staticmethod
    def find_available_times(kampaaja_id):

        stmt = text(' SELECT "Kampaaja".id, "Aika".id, "Aika".pvm, "Aika".aika_h, "Aika".aika_min FROM "Kampaaja"'
                    ' LEFT JOIN "Aika" ON "Aika".kampaaja_id = "Kampaaja".id'
                    ' WHERE ("Kampaaja".id = %s AND "Aika".vapaa = 1)'
                    ' ORDER BY "Aika".pvm' % (kampaaja_id))
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "aika_id":row[1], "pvm":row[2], "aika_h":row[3], "aika_min":row[4]})

        if len(response) < 1:
            return None
        
        return response

    @staticmethod
    def find_reservations(kampaaja_id):
        stmt = text(' SELECT "Varaus".id, "Aika".pvm, "Aika".aika_h, "Aika".aika_min, "Asiakas".firstName FROM "Kampaaja" '
                    ' JOIN "Varaus" ON "Varaus".kampaaja_id = "Kampaaja".id '
                    ' JOIN "Aika" ON "Aika".id = "Varaus".aika_id '
                    ' JOIN "Asiakas" ON "Asiakas". = "Varaus".asiakas_id '
                    ' WHERE ("Kampaaja".id = %s) ' % (kampaaja_id))
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"varaus_id":row[0], "aika_pvm":row[1], "aika_h":row[2], "aika_min":row[3], "asiakas_name":row[4]})

        if len(response) < 1:
            return None

        return response