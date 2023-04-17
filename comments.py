from db import db
from flask import session

def add_comment(content, user_id, message_id):
    sql = """INSERT INTO comments (content, user_id, message_id)
            VALUES (:content, :user_id, :message_id)"""
    db.session.execute(sql, {"content":content, "user_id":user_id, "message_id":message_id})
    db.session.commit()