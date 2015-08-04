from flask import Flask, render_template, request, redirect, url_for
from forms import FormToReverse

# Creating instances
app = Flask(__name__)
app.config.from_object('config')


def reverse(string):
    return string[::-1]


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FormToReverse(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        return redirect()
    return render_template('', error=error)

@app.route('/reversed')
def rev_str(user_input):
    rev_string = reverse(user_input)
    return render_template('',user_input=user_input, rev_input=rev_input)

@app.errorhandler(404)
def page_not_found(error):
    return render_template(''),404

@app.errorhandler(500)
def server_error(error):
    return render_template(''),500

@app.errorhandler(403)
def access_forbidden(error):
    return render_template(''),403
    

if __name__=='__main__':
    app.run(debug=True)
