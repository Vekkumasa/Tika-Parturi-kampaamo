from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import NumberRange

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
    firstName = StringField("Etunimi", [validators.Length(min=3)])
    lastName = StringField("Sukunini", [validators.Length(min=3)])
    phoneNumber = StringField("Puhelinnumero", [validators.Length(min=3)])
    class Meta:
        csrf = False

class AikaForm(FlaskForm):
    pvm = DateField('DatePicker', format='%Y-%m-%d')
    aika_h = IntegerField("Hour", validators=[NumberRange(min=0, max=24, message='bla')])
    aika_min = IntegerField("Minutes", validators=[NumberRange(min=0, max=60, message='blabla')])

    class Meta:
        csrf = False