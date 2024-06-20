from flask import flask, request, jsonify
from database import app, mongo
from models import User, Login, LinkID
from operations import create_user, authenticate_user, Link_id, delete_user

user_collection = mongo.db.users
linked_id_collection = mongo.db.linked_ids

# Registers the User


@app.route('/register', methods=['POST'])
def register():
    # gets the json data from the body and  automatically gets converted  into the dictionary
    user_data = request.json

    # This is basically used to  unpack the elements in the dictionary
    user = User(**user_data)

    if user_collection.find_one({"email": user.email}):
        # return the json object with the message and status code
        return jsonify({"error": 'Email already Registered'}), 400

    # user.dict() basically converts the code back to the dictionary
    create_user(user.dict(), user_collection)
    return jsonify({"message": "User Registered Successfully"}), 201

# logins the user


@app.route('/login', methods=['POST'])
def login():
    login_data = request.json

    login = Login(**login_data)

    # Authenticate the user Present in the database
    user = authenticate_user(login.email, login.password, user_collection)

    if not user:
        return jsonify({"error": "Invalid Credentials"})

    return jsonify({"message": " Loggin succesfull"})

# Linking Of the Id  with the user


@app.route('/link', methods=['POST'])
def Linking():
    Link_id_data = request.json
    Link_id_obj = LinkID(**Link_id_data)
    user = user_collection.find_one({"username": Link_id_obj.username})
    if not user:
        return jsonify({"error": " User not found"}), 404

    Link_id(Link_id_obj.username, Link_id_obj.linked_id, linked_id_collection)
    return jsonify({"message": " user linked successfully"}), 203


@app.route('/delete-user/username', methods=['DELETE'])
def delete(username):
    user = user_collection.find_one({"username": username})
    if not user:
        return jsonify({"error": "User not found"}), 404
    delete_user(username, user_collection, linked_id_collection)
    return jsonify({"message": "User and linked IDs deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
