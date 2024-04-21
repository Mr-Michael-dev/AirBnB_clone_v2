#!/usr/bin/python3
"""
This script starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """displays a text to the client on the default route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays a text to the client on the route /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    displays C followed by the value of the text variable
    to the client on the route /hbnb
    """
    text_with_space = text.replace("_", " ")
    return f"C {text_with_space}"


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """
    displays Python followed by the value of the text variable
    to the client on the route /hbnb
    """

    text_with_space = text.replace("_", " ")
    return f"Python {text_with_space}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    display “n is a number” only if n is an integer
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
