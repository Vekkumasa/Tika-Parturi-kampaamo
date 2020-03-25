from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.fields.html5 import DateField

class KampaajaForm(FlaskForm):
    name = StringField("Full name", [validators.Length(min=3)])
    username = StringField("Username", [validators.Length(min=3)])
    password = PasswordField("Password", [validators.Length(min=3)])
    
    class Meta:
        csrf = False

class AsiakasForm(FlaskForm):
    firstName = StringField("First name", [validators.Length(min=3)])
    lastName = StringField("Last name", [validators.Length(min=3)])
    phoneNumber = StringField("Phone number", [validators.Length(min=3)])

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    phoneNumber = StringField("Phone number")

    class Meta:
        csrf = False

class VarausForm(FlaskForm):
    date = DateField('DatePicker', format='%Y-%m-%d')
    phoneNumber = StringField("Puhelinnumero", [validators.Length(min=3)])
    class Meta:
        csrf = False
