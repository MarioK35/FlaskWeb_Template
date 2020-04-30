import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hola Mundo!"
    return render_template("index.html", headline=headline)

@app.route("/<string:name>")
def hola(name):
    name = name.capitalize()
    return f"Hola, {name}"
