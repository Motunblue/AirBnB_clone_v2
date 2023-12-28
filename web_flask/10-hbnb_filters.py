#!/usr/bin/python3
"""Start a flask web server"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Render hbnb page"""

    return render_template('10-hbnb_filters.html', states=storage.all(State),
                           amenities=storage.all(Amenity))


@app.teardown_appcontext
def teardown(exception):
    """Remove current session"""
    storage.close()


if __name__ == '__main__':
    """Run"""
    app.run(host='0.0.0.0', debug=True)
