from flask import Flask, render_template, request, \
    url_for, redirect

from forms import ReverseStringForm

app = Flask(__name__)
app.config.from_object('reverse.config')


def reverse(word):
    return word[::-1]


# routes

@app.route('/', methods=['GET', 'POST'])
def main():
    form = ReverseStringForm(request.form)
    if form.validate_on_submit():
        text = form.reverse_string.data
        return redirect(url_for('reverse_string', user_input=text))
    return render_template('index.html', form=form)


@app.route('/reversed_input/<user_input>')
def reverse_string(user_input):
    reversed_string = reverse(user_input)
    return render_template(
        'reverse.html',
        input=user_input,
        output=reversed_string
    )
