from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class ReverseForm(Form):
    input = StringField('Input', validators=[DataRequired()])
