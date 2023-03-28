from db import db
from flask import session
from sqlalchemy.sql import text

def get_categories():
    sql = text("SELECT id, category_name FROM categories")
    return db.session.execute(sql).fetchall()

def get_category_name(category_id):
    sql = text("SELECT category_name FROM categories WHERE id=:id")
    result = db.session.execute(sql, {"id":category_id})
    return result.fetchone()[0]

def get_category_messages(category_id):
    sql = text("SELECT id, title, content, category_id FROM messages WHERE category_id=:id")
    result = db.session.execute(sql, {"id":category_id})
    return result.fetchall()