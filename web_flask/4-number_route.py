#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

# Ensures strict_slashes are set to False for all routes globally.
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    return "<p>Hello HBNB!</p>"


@app.route("/hbnb")
def hbnb():
    return "<p>HBNB</p>"


@app.route("/c/<text>")
def show_c_text(text):
    modified_text = text.replace('_', ' ')
    return 'C ' + modified_text


@app.route("/python")
@app.route("/python/<text>")
def show_python_text(text='is cool'):
    modified_text = text.replace('_', ' ')
    return 'Python ' + modified_text


@app.route("/number/<int:n>")
def index(n):
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
