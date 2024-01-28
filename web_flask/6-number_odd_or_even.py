#!/usr/bin/python3
"""
    Python flask script to check even and odd and display result in
    template file
"""


from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    return ('C {}'.format(escape(text.replace("_", " "))))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    return ('Python {}'.format(escape(text.replace("_", " "))))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_html(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
