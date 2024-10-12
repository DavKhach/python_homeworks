"""Bad Example"""

# class Person:
#     def _init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def save_to_file(self):
#         with open(f"{self.name}.txt", 'w') as file:
#             file.write(f"{self.name}, {self.age}")

"""The Person class is responsible for both representing person and file operations"""


"""Right example"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class FileManager:
    @staticmethod
    def save_to_file(person):
        with open(f"{person.name}.txt", 'w') as file:
            file.write(f"{person.name}, {person.age}")

pers = Person("Tom", 26)
FileManager.save_to_file(pers)


"""Now Person class only handles person data, and FileManager class only handles file operations"""
