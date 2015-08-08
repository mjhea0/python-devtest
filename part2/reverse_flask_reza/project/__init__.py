from flask import Flask, render_template, request, redirect, url_for
from project.forms import FormToReverse

app = Flask(__name__)
app.config.from_object('project.config')


def reverse(string):
    return string[::-1]


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FormToReverse(request.form)
    if form.validate_on_submit():
        return redirect(url_for('rev_str', user_input=form.reverse.data))
    return render_template('index.html', form=form)


@app.route('/reversed_input/<user_input>')
def rev_str(user_input):
    reversed_string = reverse(user_input)
    return render_template(
        'reversed.html',
        user_input=user_input,
        rev_input=reversed_string
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("500.html"), 500
