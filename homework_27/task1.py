class Person:
    __slots__ = ['name', 'age', 'email']

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"

person = Person("Jack", 42, "jack@example.com")
print(person.display_details())

# Trying to assign an attribute which is not defined in __slots__
try:
    person.password = "jack42" # This raises AttributeError
except AttributeError as e:
    print(e)
