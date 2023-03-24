from app import app
from flask import abort, render_template, redirect, request, session


@app.route("/")
def index():
    return render_template("index.html")
