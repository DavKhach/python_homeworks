class Employee:
    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary


    def get_employee_id(self):
        return self.__employee_id


    def get_name(self):
        return self.__name


    def get_salary(self):
        return self.__salary


    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id


    def set_name(self, name):
        self.__name = name


    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative. Setting to 0")
            self.__salary = 0


    employee_id = property(get_employee_id, set_employee_id)
    name = property(get_name, set_name)
    salary = property(get_salary, set_salary)


emp = Employee(1, "Tom", 30000)
print(emp.employee_id)
print(emp.name)
print(emp.salary)


emp.salary = -1000
print(emp.salary)
