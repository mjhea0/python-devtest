from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

class ReverseForm(Form):
    reverse = TextField('Reverse', validators=[DataRequired()])
