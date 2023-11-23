from config.models import users_collection


async def get_info():
    user_email = "abhi@gmail.com"

    # storing into variable
    existing_user = await users_collection.find_one({"email": user_email})

    return existing_user
