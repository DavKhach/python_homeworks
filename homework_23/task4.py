class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Enter valid age")

pers = Person("David", 23)
print(f"Current age: {pers.get_age()}")
pers.set_age(35)
print(f"Updated age: {pers.get_age()}")
