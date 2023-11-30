from config.models import users_collection
from libs.helpers import jwt_creation_fun


async def login_auth(username, password):
    try:

        current_user = users_collection.find_one({"email": username},
                                                 {"_id": 0, "password": 1})

        if current_user is None or not current_user:
            return {"authrized": False, "token": ""}

        if password != current_user["password"]:
            return {"authrized": False, "token": ""}

        token = await jwt_creation_fun()
        return {"authrized": True, "token": token}
    except Exception as err:
        return err
