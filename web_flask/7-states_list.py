#!/usr/bin/python3
"""
Script that starts a flask web application
listens to 0.0.0.0:5000
    
"""
from models import *
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display html page from 7-states_list.html"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """Close storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
