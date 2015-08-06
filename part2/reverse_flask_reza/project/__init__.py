from flask import Flask, render_template, request, redirect, url_for
from forms import FormToReverse

# Creating instances
app = Flask(__name__)
app.config.from_object('project.config')


def reverse(string):
    return string[::-1]


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FormToReverse(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('rev_str'))
    return render_template('index.html')

@app.route('/reversed/', methods=['POST'])
def rev_str():
    rev_string = reverse(request.form['user_input'])
    return render_template('reversed.html', output = rev_string, user_input=request.form['user_input'])

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'),500


if __name__=='__main__':
    app.run(debug=True)
