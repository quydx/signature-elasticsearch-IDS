from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, FieldList
from wtforms.validators import DataRequired
from pprint import pprint 


class SignatureForm(FlaskForm):
    """Signature Form Class """
    signatures = FieldList(BooleanField(''), min_entries=1)

if __name__ == '__main__':
    print('hello')


