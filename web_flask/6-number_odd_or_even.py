#!/usr/bin/python3
""" Script that starts a Flask web application"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display “HBNB” """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_hbnb(text):
    """ display “C ”, followed by the value of the text variable """
    text_result = text.replace('_', ' ')
    return f'C {text_result}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_hbnb(text="is cool"):
    """ display “Python ”, followed by the value of the text variable """
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_hbnb(n):
    """ display “n is a number” only if n is an integer """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp_hbnb(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_even_hbnb(n):
    """ display a HTML page only if n is an integer """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
