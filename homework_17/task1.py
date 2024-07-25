def greet(first_name, last_name, message="Hello"):
    full_name = f"{first_name} {last_name}"
    return f"{message} {full_name}"

print(greet("John", "Doe"))
