from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hashed(password: str) -> str:
    return pwd_context.hash(password)


def verif_password(user_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(user_password, hashed_password)


def create_user(user: dict, user_collection):
    user['password'] = get_password_hashed(user['password'])
    user_collection.insert_one(user)
    return user


def authenticate_user(email: str, password: str, user_collection):
    user = user_collection.find_one({"email": email})
    if user and verif_password(password, user['password']):
        return user
    return None


def Link_id(username: str, linked_id: str, linked_id_collection):
    linked_id_collection.insert_one({"username": username, "linked_id": linked_id})


def delete_user(username: str, user_collection, linked_id_collection):
    user = user_collection.find_one({"username": username})
    if not user:
        return None, "User not found"
    # Delete user from the user cluster
    user_collection.delete_one({"_id": user["_id"]})

    # Delete associated linked IDs
    linked_id_collection.delete_many({"user_id": user["_id"]})

    return True, "User and associated data deleted successfully"
