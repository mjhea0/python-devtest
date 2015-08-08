from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class FormToReverse(Form):
    reverse = StringField('Reverse', validators=[DataRequired(), Length(min=2)])
