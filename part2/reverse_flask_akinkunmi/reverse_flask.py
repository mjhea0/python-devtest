from flask import Flask, render_template, redirect, url_for
from flask.ext.session import Session
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from flask_wtf.csrf import CsrfProtect
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
CsrfProtect(app)
reverse_flask_session = Session


class Reverse_Flask_Form(Form):
    form_string = StringField('Please input a string', validators=[Required()])
    form_submit = SubmitField('Submit')


def reverse(str_to_reverse):
    return str_to_reverse[::-1]


@app.errorhandler(403)
def page_forbidden(e):
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def reverse_string_post():
    form = Reverse_Flask_Form()
    if form.validate_on_submit():
        input_string = form.form_string.data
        return redirect(url_for('reversed_string', entry=input_string))
    return render_template('entry_flask.html', form=form)


@app.route('/reversed_entry/<entry>')
def reversed_string(entry):
    r_string = reverse(entry)
    return render_template('reverse.html', original=entry, transformed=r_string)


if __name__ == '__main__':
    app.debug = True
    app.run()
