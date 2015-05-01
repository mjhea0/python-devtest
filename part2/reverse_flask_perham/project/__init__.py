from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        string = request.form['string']
        result = string[::-1]
        return result
    else:
        return render_template('index.html')
