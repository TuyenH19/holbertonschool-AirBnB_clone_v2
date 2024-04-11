#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from flask import Flask, render_template
from models import State, Amenity, City

app = Flask(__name__)

# Ensures strict_slashes are set to False for all routes globally.
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def filters():
    """Displays the main HBnB filters HTML page."""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    cities = storage.all(City)
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities, cities=cities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
