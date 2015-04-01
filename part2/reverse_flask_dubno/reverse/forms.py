from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, length


class ReverseStringForm(Form):
    reverse_string = StringField(
        'Reverse',
        validators=[DataRequired(), length(min=2)]
    )
