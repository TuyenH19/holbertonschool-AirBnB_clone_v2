#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models import State

app = Flask(__name__, template_folder="templates")

# Ensures strict_slashes are set to False for all routes globally.
app.url_map.strict_slashes = False


@app.route("/states")
def list_state():
    """ Display all states """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=None)


@app.route("/states/<id>")
def list_state_id(id):
    """ Display an html page with info about <id>, if it exists """
    states = storage.all(State).values()
    state = None
    for s in states:
        if s.id == id:
            state = s
            break
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
