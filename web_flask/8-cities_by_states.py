#!usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models import State, City

app = Flask(__name__, template_folder="templates")

app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def list_city_by_state():
    """ Display city list by states """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    sorted_states = sorted(states, key=lambda s: s.name, reverse=False)
    sorted_cities = sorted(cities, key=lambda c: c.name, reverse=False)
    return render_template('8-cities_by_states.html',
                           states=sorted_states,
                           cities=sorted_cities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
