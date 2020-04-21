from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, NumberRange, DataRequired

class AsiakasForm(FlaskForm):
    firstName = StringField("First name", [validators.Length(min=3)])
    lastName = StringField("Last name", [validators.Length(min=3)])
    phoneNumber = IntegerField("Phone number", [validators.Length(min=3)])

    class Meta:
        csrf = False