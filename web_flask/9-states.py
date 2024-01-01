#!/usr/bin/python3
"""Start a flask web server"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """Render state id"""
    states = storage.all(State)
    if id:
        for v in states.values():
            if v.id == id:
                return render_template('9-states.html',
                                       cities=v.cities, state=v)
        return render_template('9-states.html', notfound=True)
    else:
        return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Remove current session"""
    storage.close()


if __name__ == '__main__':
    """Run"""
    app.run(host='0.0.0.0')
