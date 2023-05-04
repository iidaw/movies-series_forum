from app import app
from flask import abort, render_template, redirect, request, session
import users, messages, categories, comments


@app.route("/")
def index():
    return render_template("index.html", categories = categories.get_categories())

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        username = request.form["username"]
        is_username_available = users.is_username_available(username)

        if is_username_available > 0:
            return render_template("error.html", message="Username is not available for use")
        
        if len(username) < 4:
            return render_template("error.html", message="Username can't be shorter than 4 characters")

        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if password1 != password2:
            return render_template("error.html", message="Passwords don't match")
        
        if len(password1) < 6:
            return render_template("error.html", message="Password must be at least 6 characters")
        
        if users.register(username, password1):
            return redirect("/")
        
        else: return render_template("error.html", message="Registering failed")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", message="Wrong username or password")

        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/newmessage", methods=["GET", "POST"])
def new_message():
    if request.method == "GET":
        return render_template("newmessage.html")
    
    if request.method == "POST":
        users.check_csrf()
        message_title = request.form["title"]

        if len(message_title) < 1:
            return render_template("error.html", message="Title can't be empty")
        content = request.form["message"]

        if len(content) < 10:
            return render_template("error.html", message="Please write at least 10 characters")
        category_id = request.form["category_id"]
        messages.add_message(message_title, content, category_id, users.user_id())
        return redirect("/")


@app.route("/category/<int:id>")
def category(id):
    category_name = categories.get_category_name(id)
    messages = categories.get_messages_cateory(id)
    return render_template("categories.html", category_name=category_name, id=id, messages=messages)

@app.route("/message/<int:id>")
def message(id):
    message = messages.get_message(id)
    comments = messages.get_message_comments(id)
    likes = messages.get_message_likes(id)
    return render_template("message.html", message=message, id=id, comments=comments, likes=likes)

@app.route("/comment", methods=["POST"])
def add_comment():
    if request.method == "POST":
        users.check_csrf()
        message_id = request.form["message_id"]
        content = request.form["content"]
        comments.add_comment(content, users.user_id(), int(message_id))
        return redirect("/message/" + str(message_id))
    
@app.route("/like_message", methods=["POST"])
def like_message():
    if request.method == "POST":
        users.check_csrf()
        message_id = request.form["message_id"]
        if messages.has_user_liked_message(message_id, users.user_id()) == True:
            return render_template("error.html", message="You have already liked this")
        else:
            messages.like_message(message_id, users.user_id())
    return redirect("/message/" + str(message_id))