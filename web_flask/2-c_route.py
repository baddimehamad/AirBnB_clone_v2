#!/usr/bin/python3
"""
    Python Flask script that starts up and applications and
    creates two routes / amd /hbnb
"""

from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def home_hbnb():
    return ("HBNB")


@app.route('/c/<text>')
def c_isfun(text):
    return ('C {}'.format(escape(text.replace("_", " "))))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
