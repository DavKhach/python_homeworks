class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"My name is {self.name}, I'm {self.age} years old")


pers = Person()
pers.set_details("David", 23)
pers.display_details()
