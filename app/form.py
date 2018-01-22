from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import DataRequired

class SignatureSetting(FlaskForm):
    checkField = BooleanField()
