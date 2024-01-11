#!/usr/bin/python3
"""
    Python flask script to create routes
    to states
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=True)
def states():
    states = storage.all(State)
    return render_template("9-states.html", states=states, query_with='all')


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    for state in storage.all("State").values():
        if (state.id == id):
            return render_template("9-states.html", query_with='id')
        return render_template("9-states.html", states=state, query_with=None)


@app.teardown_appcontext
def teardown_db(self):
    """ database teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
