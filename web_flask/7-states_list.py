#!usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models import State

app = Flask(__name__, template_folder="templates")

# Ensures strict_slashes are set to False for all routes globally.
app.url_map.strict_slashes = False


@app.route("/states_list")
def list_state():
    """ Display state list with sorting"""
    states = storage.all(State).values()
    return render_template('7-states_list.html',
                           states=sorted(states, key=lambda s: s.name,
                                         reverse=False))


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
