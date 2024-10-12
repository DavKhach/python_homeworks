"""Bad Example"""

# class Worker:
#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role
#
#     def calculate_bonus(self):
#         if self.role == "developer":
#             return self.salary * 0.5
#         elif self.role == "HR":
#             return self.salary * 0.2

"""We modify calculate_bonus method every time we a new role"""


"""Right example"""
class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        raise NotImplementedError("This method should be overridden by subclass")

class Developer(Worker):
    def calculate_bonus(self):
        return self.salary * 0.5

class HR(Worker):
    def calculate_bonus(self):
        return self.salary * 0.2

dev = Developer("Jack", 35000)
hr = HR("Sara", 30000)
print(dev.calculate_bonus())
print(hr.calculate_bonus())

"""Now we extend the functionality by adding new classes without modifying existing ones"""
