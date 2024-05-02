#!/usr/bin/python3

"""Import flask"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Starts a flask web application"""
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def display_c(text):
    route_text = escape(text).replace("_", " ")
    return f"C {route_text}"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
