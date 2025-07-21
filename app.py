from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}

# Home route
@app.route("/")
def home():
    return "Welcome to User API built with Flask!"

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET one user by ID
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# POST - Add new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user_id = data.get("id")
    name = data.get("name")
    email = data.get("email")
    users[user_id] = {"name": name, "email": email}
    return jsonify({"message": "User added successfully"}), 201

# PUT - Update existing user
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id in users:
        data = request.json
        users[user_id]["name"] = data.get("name")
        users[user_id]["email"] = data.get("email")
        return jsonify({"message": "User updated"})
    else:
        return jsonify({"error": "User not found"}), 404

# DELETE - Remove  user
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    else:
        return jsonify({"error": "User not found"}), 404

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
