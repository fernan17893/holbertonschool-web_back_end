#!/usr/bin/env python3
"""Basic Flask APP"""


from flask import Flask, jsonify, request
from auth import Auth
import bcrypt


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_request() -> str:
    """Get Flask JSON payload"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """Register user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    

def valid_login(email: str, password: str) -> bool:
    """Check if login is valid"""
    if bcrypt.checkpw(password.encode('utf-8'),
        AUTH._db.find_user_by(
        email=email).hashed_password):
        return True
    else:
        return False


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
