#!/usr/bin/python3
""" Starts a Flask Web Application """
from models import storage
from models.state import State
from os import environ
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_state(id=""):
    """  an HTML page with a list of cities by states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    found = 0
    state = ""
    cities = []
    for ind in states:
        if id == ind.id:
            state = ind
            found = 1
            break
    if found:
        states = sorted(state.cities, key=lambda k: k.name)
        state = state.name
    if id and not found:
        found = 2
    return render_template('9-states.html', state=state,
                           array=states, found=found)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
