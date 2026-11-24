import jwt
from flask import Blueprint, jsonify, request

from app.db import get_connection
from app.utils.mailer import send_email
from app.utils.security import hash_password

auth = Blueprint("auth", __name__)


@auth.post("/auth/login")
def login():
    body = request.json
    cursor = get_connection().cursor()
    cursor.execute(
        "SELECT id FROM users WHERE email = ? AND password_hash = ?",
        (body["email"], hash_password(body["password"])),
    )
    row = cursor.fetchone()
    if row is None:
        return jsonify({"error": "invalid credentials"}), 401
    token = jwt.encode({"sub": row[0]}, "shop-jwt-signing-secret-2024", algorithm="HS256")
    return jsonify({"token": token})


@auth.post("/auth/forgot-password")
def forgot_password():
    email = request.json["email"]
    send_email(email, "Reset your password", "Use the link in this email to reset your password.")
    return jsonify({"sent": True})
