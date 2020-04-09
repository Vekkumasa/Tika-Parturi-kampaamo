from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, NumberRange, DataRequired

class VarausForm(FlaskForm):
    firstName = StringField("Etunimi", [validators.Length(min=3)])
    lastName = StringField("Sukunini", [validators.Length(min=3)])
    phoneNumber = StringField("Puhelinnumero", [validators.Length(min=3)])
    submit = SubmitField("Submit")
    class Meta:
        csrf = False


class DeleteForm(FlaskForm):
    varausID = BooleanField("VarausID")

    class Meta:
        csrf = False