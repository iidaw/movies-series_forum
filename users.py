import os
from db import db
from flask import session, request, abort
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text

def register(username, password):
    hash_value = generate_password_hash(password)

    try:
        sql = text("INSERT INTO users (username,password) VALUES (:username,:password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)


def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = username
            session["csrf_token"] = os.urandom(16).hex()
            return True
        else:
            return False
        
def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)


def user_id():
    return session.get("user_id")

def logout():
    del session["user_id"]
    del session["username"]

def is_username_available(username):
    sql = text("SELECT COUNT (*) FROM users WHERE username=:username")
    result= db.session.execute(sql, {"username":username})

    return result.fetchone()[0]