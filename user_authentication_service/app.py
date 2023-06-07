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


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """Login"""
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        Flask.abort(401)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
