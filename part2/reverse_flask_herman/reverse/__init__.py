# reverse/__init__.py


from flask import Flask, render_template, request, \
    flash, url_for, redirect

from reverse.forms import ReverseStringForm


################
#### config ####
################

app = Flask(__name__)
app.config.from_object('reverse.config')


#################
#### helpers ####
#################

def reverse(string):
    result = ""
    for letter in range(len(string), 0, -1):
        result = result + string[letter-1]
    return result


################
#### routes ####
################

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
