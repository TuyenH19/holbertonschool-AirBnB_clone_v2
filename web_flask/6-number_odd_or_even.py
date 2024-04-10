#!/usr/bin/python3
"""Flask web application

Returns:
    display template of odd or even number
"""

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

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


@app.route("/python")
@app.route("/python/<text>")
def show_python_text(text='is cool'):
    """ Display Python followed by a text with default value """
    modified_text = text.replace('_', ' ')
    return 'Python ' + modified_text


@app.route("/number/<int:n>")
def index(n):
    """ Display a only number """
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def num_template(n):
    """ Display a number template """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_even_template(n):
    """ Display template of odd or even number """
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, text="even")
    else:
        return render_template('6-number_odd_or_even.html', n=n, text="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
