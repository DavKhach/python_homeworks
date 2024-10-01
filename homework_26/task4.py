class Descriptor:
    def __init__(self):
        self.__score = None

    def __get__(self, instance, owner):
        return self.__score

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Score must be integer")
        if value < 0 or value > 100:
            raise ValueError("Score must be between 0 and 100")
        self.__score = value

class Student:
    score = Descriptor()

    def __init__(self, name, score):
        self.name = name
        self.score = score


try:
    student = Student("Tom", 75)
    print(f"{student.name}'s score is {student.score}")

    student.score = 110
except ValueError as e:
    print(e)
