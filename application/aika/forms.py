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
    aika = SubmitField("Poista aika")

    class Meta:
        csrf = False

class WorkDayForm(FlaskForm):
    pvm = DateField('Date', format='%Y-%m-%d')
    aloitusAika = IntegerField("aloitusAika", validators=[NumberRange(min=9, max=15, message='Aloitusaika oltava 9 ja 15 välillä')])
    kesto = IntegerField("kesto", validators=[NumberRange(min=1, max=16, message='Arvo 1-16 välillä')])
