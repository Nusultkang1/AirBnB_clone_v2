#!/usr/bin/python3
"""
Python code to start a flask web application
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
"""

from flask import Flask

app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/', strict_slashes=False)
def hbnb_route():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
