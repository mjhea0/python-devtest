from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap
from .forms import ReverseForm

app=Flask(__name__)
app.config.from_pyfile('_config.py')
Bootstrap(app)

@app.route('/',methods=['POST','GET'])
def index():
    error = None
    form = ReverseForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            input_string=request.form['input']
            return render_template('index.html',form=form,reversed_string=input_string[::-1])
    return render_template('index.html',form=form,error=error)
