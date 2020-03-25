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

    @staticmethod
    def find_available_times():
        stmt = text("SELECT Kampaaja.id, Aika.pvm FROM Kampaaja"
                    " LEFT JOIN Aika ON Aika.kampaaja_id = Kampaaja.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "pvm":row[1]})

        return response