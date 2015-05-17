# run.py

import os
from project.reverse_flask import app

host = '0.0.0.0'
port = int(os.environ.get('PORT', 5000))

if app.config['DEBUG'] == True:
    app.run()
else:
    app.run(host=host, port=port)