set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1 | set2
print("Union: ", union_set)

intersection_set = set1 & set2
print("Intersection: ", intersection_set)

sym_diff_set = set1 ^ set2
print("Symmetric Difference: ", sym_diff_set)





users_dict = {}

while True:
    id = input("Enter Id (or 'exit' to finish): ")
    if id.lower() == 'exit':
        break
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    phone = input("Enter phone number: ")

    user_data = {
            "ID": id,
            "Name": name,
            "Surname": surname,
            "Email": email,
            "Password": password,
            "Phone": phone
    }

    if name in users_dict:
        users_dict[name].append(user_data)
    else:
        users_dict[name] = [user_data]


search_name = input("Enter name to search: ")

if search_name in users_dict:
    found_users = users_dict[search_name]
    for user in found_users:
        print("\nUser found: ")
        for key, value in user.items():
            print(f"{key}: {value}")
else:
    print("Not found")
