#!/usr/bin/python3
"""
A simple Flask API with GET and POST endpoints.
"""

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route("/")
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Status endpoint"""
    return "OK"


@app.route("/data")
def get_usernames():
    """Return a list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return the full object for a given username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST request"""
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Create user object
    user_obj = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    # Store in memory
    users[username] = user_obj

    return jsonify({"message": "User added", "user": user_obj}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
