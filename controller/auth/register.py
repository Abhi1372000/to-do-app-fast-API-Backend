from config.models import users_collection


async def register_to_db(username, password, name, occupation):
    user_data = {
        "email": username,
        "password": password,
        "name": name,
        "occupation": occupation,
        "todo_list": {}
    }
    registration = users_collection.insert_one(user_data)
    print(registration)
    return "register_to_db"
