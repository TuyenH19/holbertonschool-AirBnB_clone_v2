#!/usr/bin/python3
"""Flask web application

Returns:
    display C followed by a text
"""

from flask import Flask

app = Flask(__name__)

# Ensures strict_slashes are set to False for all routes globally.
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """ Display Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Display HBNB """
    return "HBNB"


@app.route("/c/<text>")
def show_c_text(text):
    """ Display C followed by a text """
    modified_text = text.replace('_', ' ')
    return 'C ' + modified_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
