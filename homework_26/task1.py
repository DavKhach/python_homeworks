class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must positive")
        self.__age = value

try:
    p = Person("Tom", 26)
    print(f"{p.name}'s age is {p.age}")

    p.age = -5
except ValueError as e:
    print(e)
