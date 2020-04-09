from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, NumberRange, DataRequired

class AikaForm(FlaskForm):
    pvm = DateField('Date', format='%Y-%m-%d')
    aika_h = IntegerField("Hour", validators=[NumberRange(min=0, max=24, message='Arvo 0-24 välillä')])
    aika_min = IntegerField("Minutes", validators=[NumberRange(min=0, max=60, message='Arvo 0-60 välillä')])

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    pvm = DateField('Date', format='%Y-%m-%d')
    aika_h = IntegerField("Hour", validators=[NumberRange(min=0, max=24, message='Arvo 0-24 välillä')])
    aika_min = IntegerField("Minutes", validators=[NumberRange(min=0, max=60, message='Arvo 0-60 välillä')])

    class Meta:
        csrf = False

class DeleteTimeForm(FlaskForm):
    aikaID = BooleanField("AikaID")

    class Meta:
        csrf = False