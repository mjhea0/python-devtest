# Reverse a string
# Note - this doesn't persist anything in a db

import os

# import specific reverse function
import sys
sys.path.insert(0, '../../part1/reverse-string/reverse_afr/')
from  reverse import reverse

from flask import Flask, flash, redirect, render_template, request, url_for

SECRET_KEY = "jiosf0m()(HJI890w23r9j*&*^&GY"
WTF_CSRF_ENABLED = True # cross-site request forgery protection

app = Flask(__name__)
app.config.from_object(__name__)

# Main index route
@app.route("/")
def index():
  return render_template("index.html")

# Route to reversed entry
@app.route("/reverse_entry", methods = ["POST"])
def reverse_entry():
  re = reverse(request.form["string_to_reverse"])
  return render_template("reverse_entry.html", re = re)

# Main - port added to work with heroku
if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port = port)
