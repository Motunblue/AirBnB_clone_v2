#!/usr/bin/python3
"""Start a flask web server"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Render State list"""
    return render_template('7-states_list.html', states=storage.all(State))


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Render cities by state"""
    return render_template('8-cities_by_states.html', states=storage.all(State))


@app.teardown_appcontext
def teardown(exception):
    """Remove current session"""
    storage.close()


if __name__ == '__main__':
    """Run"""
    app.run(host='0.0.0.0')
