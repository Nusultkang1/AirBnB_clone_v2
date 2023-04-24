#!/usr/bin/python3
"""
Script that starts a flask web application
The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import *
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=None):
    states = storage.all("State")
    if state_id is not None:
        state_id = "State." + state_id
    return render_template("9-states.html", states=states, state_id=state_id)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
