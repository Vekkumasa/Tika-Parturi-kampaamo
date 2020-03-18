from application import db
from application.models import Base

class Kampaaja(Base):

    firstName = db.Column(db.String(144), nullable=False)
    lastName = db.Column(db.String(144), nullable=False)

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
