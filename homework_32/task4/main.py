import json


with open("user_data.json", "r") as file:
    user_data = json.load(file)

filtered_users = [user for user in user_data if user.get("age") > 30 and user.get("role") == "manager"]

with open("filtered_users.json", "w") as file:
    json.dump(filtered_users, file, indent=4)
