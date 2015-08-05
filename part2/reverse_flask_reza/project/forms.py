from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class FormToReverse(Form):
    string = StringField('reverse', validators=[DataRequired(), Length(min=4)])


