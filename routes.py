from app import app
from flask import abort, render_template, redirect, request, session
import users


@app.route("/")
def index():
    return render_template("index.html", messages=list)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        username = request.form["username"]
        is_username_available = users.is_username_available(username)

        if is_username_available > 0:
            return render_template("error.html", message="Username is not available for use")

        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if password1 != password2:
            return render_template("error.html", message="Passwords don't match")
        
        else: return render_template("error.html", message="Register was unsuccesfull")

@app.route("/login")
def login():
    if request.method == "GET":
        return render_template("login.html")

@app.route("/logout")
def logout():
    if request.method == "GET":
        return render_template("logout.html")

@app.route("/newmessage")
def new_message():
    if request.method == "GET":
        return render_template("newmessage.html")

@app.route("/categories")
def categories():
    if request.method == "GET":
        return render_template("categories.html")
