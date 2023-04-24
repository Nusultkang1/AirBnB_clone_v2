#!/usr/bin/python3
"""
Script that starts a flask web application
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
    /python/(<text>): display “Python ”, followed by the value of the text variable
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hbnb_route():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return "C %s" % text

@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    text = text.replace("_", " ")
    return "Python %s" % text

if __name__ = "__main__":
    app.run(host="0.0.0.0")
