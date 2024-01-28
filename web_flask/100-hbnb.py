#!/usr/bin/python3
"""
    python flask script to use db content on HNBN
"""


from flask import Flask, render_template
from models import storage
from models import *


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = storage.all("State").values()
    cities = storage.all("City").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    return render_template("100-hbnb.html", states=states, cities=cities,
                           amenities=amenities, places = places)


if __name__ == ("__main__"):
    app.run(host='0.0.0.0', port=5000, debug=False)
