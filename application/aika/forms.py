from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, NumberRange, DataRequired

class AikaForm(FlaskForm):
    pvm = DateField('Date', format='%Y-%m-%d')
    aika_h = IntegerField("Hour", validators=[NumberRange(min=0, max=23, message='Arvo 0-23 välillä')])
    aika_min = IntegerField("Minutes", validators=[NumberRange(min=0, max=60, message='Arvo 0-60 välillä')])

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    pvm = DateField('Date', format='%Y-%m-%d')
    aika_h = IntegerField("Hour", validators=[NumberRange(min=0, max=23, message='Arvo 0-23 välillä')])
    aika_min = IntegerField("Minutes", validators=[NumberRange(min=0, max=60, message='Arvo 0-60 välillä')])

    class Meta:
        csrf = False

class DeleteTimeForm(FlaskForm):
    aika = SubmitField("Poista aika")

    class Meta:
        csrf = False

class WorkDayForm(FlaskForm):
    pvm = DateField('Date', format='%Y-%m-%d')
    aloitusAika = IntegerField("Hour", validators=[NumberRange(min=0, max=23, message='Arvo 0-23 välillä')])
    kesto = IntegerField("Minutes", validators=[NumberRange(min=1, max=9, message='Arvo 1-9 välillä')])

    class Meta:
        csrf = False
