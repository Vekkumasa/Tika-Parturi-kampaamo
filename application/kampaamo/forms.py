from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, NumberRange, DataRequired

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

class VarausForm(FlaskForm):
    firstName = StringField("Etunimi", [validators.Length(min=3)])
    lastName = StringField("Sukunini", [validators.Length(min=3)])
    phoneNumber = StringField("Puhelinnumero", [validators.Length(min=3)])
    class Meta:
        csrf = False

class AikaForm(FlaskForm):
    pvm = DateField('Date', format='%Y-%m-%d')
    aika_h = IntegerField("Hour", validators=[NumberRange(min=0, max=24, message='Arvo 0-24 välillä')])
    aika_min = IntegerField("Minutes", validators=[NumberRange(min=0, max=60, message='Arvo 0-60 välillä')])

    class Meta:
        csrf = False

class DeleteForm(FlaskForm):
    varausID = BooleanField("VarausID")

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    pvm = DateField('Date', format='%Y-%m-%d')
    aika_h = IntegerField("Hour", validators=[NumberRange(min=0, max=24, message='Arvo 0-24 välillä')])
    aika_min = IntegerField("Minutes", validators=[NumberRange(min=0, max=60, message='Arvo 0-60 välillä')])

    class Meta:
        csrf = False