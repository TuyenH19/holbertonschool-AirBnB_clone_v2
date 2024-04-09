#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

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


@app.route("/number_template/<int:n>")
def num_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
