from application import db

class Kampaaja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    firstName = db.Column(db.String(144), nullable=False)
    lastName = db.Column(db.String(144), nullable=False)

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
