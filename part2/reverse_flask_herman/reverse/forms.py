# reverse/forms.py


from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, length


class ReverseStringForm(Form):
    reverse_string = TextField(
        'Reverse', validators=[DataRequired(), length(min=2)])
