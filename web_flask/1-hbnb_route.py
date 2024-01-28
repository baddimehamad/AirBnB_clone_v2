#!/usr/bin/python3
"""
    Python Flask script that starts up and applications and
    creates two routes / amd /hbnb
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ returning the result"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def home_hbnb():
    """ working on the file"""
    return ("HBNB")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
