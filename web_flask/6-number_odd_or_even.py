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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display n if it's a number"""
    return (f'{n} is a number')


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """Displace html template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Display odd or even template"""
    if (n % 2) == 0:
        return render_template('6-number_odd_or_even.html',
                               n=n, type="is even")
    else:
        return render_template('6-number_odd_or_even.html', n=n, type="is odd")


if __name__ == '__main__':
    """Run"""
    app.run(host='0.0.0.0')
