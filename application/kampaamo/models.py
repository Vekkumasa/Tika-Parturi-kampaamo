from application import db
from application.models import Base

class Kampaaja(Base):

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

class Asiakas(Base):

    phoneNumber = db.Column(db.String(144))

    def __init__(self, firstName, lastName, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber