#!/usr/bin/python3
"""Start a flask web server"""
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Return Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbhb():
    """Return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """Return C with text variable"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text="is cool"):
    """Return python with text variable"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/', strict_slashes=False)
@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if type(eval(n)) == int:
        return (f'{n} is a number')


@app.route('/number_template/', strict_slashes=False)
@app.route('/number_template/<n>', strict_slashes=False)
def template(n):
    """Displace html template"""
    if type(eval(n)) == int:
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """Run"""
    app.run(host='0.0.0.0')
