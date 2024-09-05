class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"My name is {self.name}, I'm {self.age} years old")


person = Person("David", 23)
person.display_details()
