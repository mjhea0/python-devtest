from flask import Flask, render_template, request

app = Flask(__name__)

app.config['DEBUG'] = False


@app.route('/')
def get_string():
    return render_template('index.html')


@app.route('/reverse_string', methods=['POST'])
def reverse_string():
    return render_template(
        'result.html',
        original_str=request.form['str_to_reverse'],
        result=request.form['str_to_reverse'][::-1]
    )
