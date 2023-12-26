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


if __name__ == '__main__':
    """Run"""
    app.run(host='0.0.0.0')