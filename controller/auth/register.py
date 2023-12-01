from config.models import users_collection
from libs.helpers import password_Hash
from libs.helpers import jwt_creation_fun


async def register_to_db(username, password, name, occupation):
    try:
        hashed_password = await password_Hash(password)

        user_data = {
            "email": username,
            "password": hashed_password,
            "name": name,
            "occupation": occupation,
            "todo_list": {}
        }

        registration = users_collection.insert_one(user_data)

        if registration.acknowledged is False:
            return {"authrized": False, "token": ""}

        token = await jwt_creation_fun(username)

        return {"authrized": True, "token": token}
    except Exception as err:
        return err
