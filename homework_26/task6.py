class SalaryDescriptor:
    def __init__(self, max_salary):
        self.max_salary = max_salary
        self.__salary = None

    def __get__(self, instance, owner):
        return self.__salary

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Salary must be number")
        if value < 0:
            raise ValueError("Salary must be positive")
        if value > self.max_salary:
            raise ValueError(f"Salary cannot be exceed {self.max_salary}")
        self.__salary = value

class Employee:
    salary = SalaryDescriptor(max_salary=300000)

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

try:
    emp = Employee("Tom", 50000)
    print(f"{emp.name}'s salary: {emp.salary}")

    emp.salary = 1000000
except ValueError as e:
    print(e)
