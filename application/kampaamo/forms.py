from flask_wtf import FlaskForm
from wtforms import StringField, validators

class KampaajaForm(FlaskForm):
    firstName = StringField("First name", [validators.Length(min=3)])
    lastName = StringField("Last name", [validators.Length(min=3)])

    class Meta:
        csrf = False