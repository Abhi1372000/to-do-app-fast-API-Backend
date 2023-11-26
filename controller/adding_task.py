from datetime import datetime
from config.models import users_collection


async def add_task_to_user():
    # Find the user by email (assuming email is unique)
    try:
        user_email = "abhi@gmail.com"

        new_task = {"Learn MongoDB": ["pending", str(datetime.utcnow())]}

        # storing into variable
        existing_user = users_collection.find_one({"email": user_email})

        # updating the dictionary
        existing_user['todo_list'].update(new_task)

        # updating it to the db
        updated_result = (
            users_collection.update_one({"email": user_email}, {"$set": existing_user}))
        if updated_result.acknowledged:
            return existing_user
        return False
    except Exception as err:
        return err
