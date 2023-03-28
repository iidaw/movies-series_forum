from db import db
from flask import session
from sqlalchemy.sql import text

def get_categories():
    sql = text("SELECT id, category_name FROM categories")
    return db.session.execute(sql).fetchall()