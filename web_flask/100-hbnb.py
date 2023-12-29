#!/usr/bin/python3
"""Start a flask web server"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Render hbnb page"""

    return render_template('100-hbnb.html', states=storage.all(State),
                           amenities=storage.all(Amenity),
                           places=storage.all(Place))


@app.teardown_appcontext
def teardown(exception):
    """Remove current session"""
    storage.close()


if __name__ == '__main__':
    """Run"""
    app.run(host='0.0.0.0')
