#!/usr/bin/env python3
""" Basic flask app
"""
from flask import Flask, jsonify, request, make_response, abort
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def index():
    """ Home route
    """
    payload = {"message": "Bienvenue"}
    return jsonify(payload)


@app.route("/users", methods=['POST'])
def users():
    """ User registration
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = None
        try:
            user = AUTH.register_user(email, password)
        except ValueError:
            return jsonify({"message": "email already registered"}), 400
        except Exception as err:
            pass
        if user:
            payload = {
                "email": email,
                "message": "user created"
            }
            return jsonify(payload)


@app.route('/sessions', methods=['POST'])
def login():
    """ Login route
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if AUTH.valid_login(email, password):
            session_id = None
            session_id = AUTH.create_session(email)
            payload = {
                "email": email,
                "message": "logged in"
            }
            response = make_response(payload)
            response.set_cookie("session_id", session_id)
            return response
        else:
            abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
