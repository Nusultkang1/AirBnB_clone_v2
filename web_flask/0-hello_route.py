#!/usr/bin/python3
"""
Python script to start a Flask web application and display text:
    'Hello HBNB!'
Route '/' displays "Hello HBNB!"
Listening on 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
