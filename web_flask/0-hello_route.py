#!/usr/bin/python3
"""Python flask scritp to dispplay Hello HBNB!"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Return this to get request"""
    return ("Hello HBNB!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
