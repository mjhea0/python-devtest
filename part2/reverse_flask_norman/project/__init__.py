from flask import Flask, render_template, request, redirect, url_for
from forms import ReverseForm

app = Flask(__name__)
app.config.from_object('project.config')


def reverse(string):
    reverse_string = ""
    for i in xrange(len(string)):
        reverse_string = reverse_string + string[(len(string)-1)-i]
    return reverse_string


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ReverseForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for('rev_string', user_input=form.reverse.data))
    return render_template('index.html', form=form)


@app.route('/reversed_input/<user_input>')
def rev_string(user_input):
    reversed_string = reverse(user_input)
    return render_template(
        'reversed.html',
        user_input=user_input,
        rev_input=reversed_string
    )


@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500
