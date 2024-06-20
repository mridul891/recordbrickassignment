from flask import flask, request, jsonify
from database import app, mongo
from models import User, Login, LinkID
from operations import create_user, authenticate_user, Link_id, delete_user

user_collection = mongo.db.users
linked_id_collection = mongo.db.linked_ids


@app.routes('/register', methods=['POST'])
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


@app.routes('/login', methods=['POST'])
def login():
    login_data = request.json

    login = Login(**login_data)

    user = authenticate_user(login.email, login.password, user_collection)

    if not user:
        return jsonify({"error": "Invalid Credentials"})

    return jsonify({"message": " Loggin succesfull"})
