from flask import Blueprint, jsonify, request

from app.db import get_connection

users = Blueprint("users", __name__)


@users.get("/users/search")
def search_users():
    name = request.args.get("name", "")
    cursor = get_connection().cursor()
    cursor.execute(f"SELECT id, name, email FROM users WHERE name LIKE '%{name}%'")
    return jsonify(cursor.fetchall())
