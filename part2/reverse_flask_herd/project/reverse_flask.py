from flask import Flask, render_template, request
import os

app = Flask(__name__)

app.config['DEBUG'] = False


@app.route('/')
def get_string():
    return render_template('index.html')


@app.route('/reverse_string', methods=['POST'])
def reverse_string():
    str_to_reverse = request.form['str_to_reverse']
    return render_template(
        'result.html',
        result=str_to_reverse[::-1]
    )