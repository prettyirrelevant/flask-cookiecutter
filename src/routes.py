# Pretty much routes you don't want to create blueprints for goes here
from flask import current_app as app


@app.route("/")
def dummy():
    return "Hello"
