from app import app
from flask import abort, render_template, redirect, request, session


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    pass

@app.route("/login")
def login():
    pass

@app.route("/logout")
def logout():
    pass

@app.route("newmessage")
def new_message():
    pass

@app.route("/categories")
def categories():
    pass
