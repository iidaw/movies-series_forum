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
    sql = text("SELECT M.content, U.username FROM messages M, users U WHERE M.user_id=U.id ORDER BY M.id")
    result = db.session.execute(sql)
    return result.fetchall()