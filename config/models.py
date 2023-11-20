from pymongo import MongoClient

# creating a client
client = MongoClient('mongodb://localhost:27017/')


# Accessing the database
db = client['user']

# Accessing the collection
users_collection = db['users']

user_data = {
    "email": "nitin@gmail.com",
    "password": "nitin1372",
    "name": "Nitin",
    "occupation": "SDE-2",
    "todo_list": {
        "Learn Nextjs": [
            "pending",
            "dateCreated"
        ],
        "Learn ReactNative": [
            "done",
            "dateCreated"
        ]
    }
}

if __name__ == "__main__":
    # Insert data into the collection
    users_collection.insert_one(user_data)
    print("Done")
