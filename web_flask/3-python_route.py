#!/usr/bin/python3
""" Script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """  display “Hello HBNB!” """
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
    """ display “Python ”, followed by the value of the text """
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
