from db import db
from flask import session

def get_categories():
    sql = "SELECT id, category_name FROM categories"
    return db.session.execute(sql).fetchall()