from db import db
from flask import session
from sqlalchemy.sql import text
import users

def add_message(title, content, category_id, user_id):
    sql = text("""INSERT INTO messages (title, content, visible, category_id, user_id)
            VALUES (:title, :content, TRUE, :category_id, :user_id) RETURNING id""")
    result = db.session.execute(sql, {"title":title, "content":content, "category_id":category_id, "user_id":user_id}).fetchone()[0]
    db.session.commit()
    return result

def get_messages():
    sql = text("""SELECT M.title, M.content, U.username, C.category_name FROM messages M, users U, categories C 
            WHERE M.user_id=U.id AND M.category_id=C.id ORDER BY M.id""")
    result = db.session.execute(sql)
    return result.fetchall()

def get_message(message_id):
    sql = text("SELECT M.title, M.content, M.user_id, U.username FROM messages M INNER JOIN users U ON M.user_id=U.id WHERE M.id=:message_id")
    result = db.session.execute(sql, {"message_id":message_id})
    return result.fetchall()

def get_message_comments(message_id):
   sql = text("SELECT C.id, C.content, C.user_id, U.username FROM comments C INNER JOIN users U ON C.user_id=U.id WHERE C.message_id=:message_id ORDER BY C.id")
   result = db.session.execute(sql, {"message_id":message_id})
   return result.fetchall()

def like_message(message_id, liker_id):
    sql = text("INSERT INTO likes (message_id, liker_id) VALUES (:message_id, :liker_id)")
    db.session.execute(sql, {"message_id":message_id, "liker_id":liker_id})
    db.session.commit()

def get_message_likes(message_id):
    sql = text("SELECT COUNT(*) FROM likes WHERE message_id=:message_id")
    result = db.session.execute(sql, {"message_id":message_id})
    return result.fetchone()[0]

def has_user_liked_message(message_id, liker_id):
    sql = text("SELECT * FROM likes WHERE message_id=:message_id AND liker_id=:liker_id")
    result = db.session.execute(sql, {"message_id":message_id, "liker_id":liker_id})
    all_results = result.fetchall()
    if len(all_results) == 0:
        return False
    else:
        return True
