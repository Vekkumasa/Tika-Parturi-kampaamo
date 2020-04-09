from application import db
from sqlalchemy.sql import text

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                    onupdate=db.func.current_timestamp())
    
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    varaukset = db.relationship("Varaus", backref='User', lazy=True)
    vapaat_ajat = db.relationship("Aika", backref='User', lazy=True)
    

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

    @staticmethod
    def find_available_times(kampaaja_id):
        stmt = text("SELECT User.id, Aika.id, Aika.pvm, aika_h, aika_min FROM User"
                    " LEFT JOIN Aika ON Aika.kampaaja_id = User.id"
                    " WHERE (User.id = %s AND Aika.vapaa = 1)"
                    " GROUP BY Aika.pvm" % kampaaja_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "aika_id":row[1], "pvm":row[2], "aika_h":row[3], "aika_min":row[4]})

        return response

    @staticmethod
    def find_reservations(kampaaja_id):
        stmt = text("Select varaus.id, aika.pvm, aika.aika_h, aika.aika_min, asiakas.firstName from %s"
                    " LEFT JOIN Varaus ON Varaus.kampaaja_id = User.id"
                    " LEFT JOIN Aika ON Aika.id = Varaus.aika_id "
                    " LEFT JOIN Asiakas ON Asiakas.phoneNumber = Varaus.asiakas_id"
                    " WHERE (Kampaaja.id = %s)" % ("User" ,kampaaja_id))
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"varaus_id":row[0], "aika_pvm":row[1], "aika_h":row[2], "aika_min":row[3], "asiakas_name":row[4]})

        return response

        