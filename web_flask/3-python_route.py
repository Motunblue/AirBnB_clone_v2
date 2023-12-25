#!/usr/bin/python3
"""Start a flask web server"""
from flask import Flask

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


@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text):
    """Return python with text variable"""
    if not text:
        return "Python is cool"
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == '__main__':
    """Run"""
    app.run(host='0.0.0.0')
