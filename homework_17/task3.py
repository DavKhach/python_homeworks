def person(first_name, last_name, *, age, city):
    profile = f"{first_name}, {last_name}, {age}, {city}"
    return profile
print(person("John", "Doe", age="20", city="Los-Angeles"))
