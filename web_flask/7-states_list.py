#!/usr/bin/python3
""" Scrip that starts a flask web app """
from models import storage
from models.state import State
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.teardown_appcontext
def hbnb_db(error):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display a HTML page """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
