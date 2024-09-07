class Student:
    def __init__(self, name, roll_number):
        self.__name = name
        self.__roll_number = roll_number
        self.__grades = []

    def get_name(self):
        return self.__name

    def get_roll_number(self):
        return self.__roll_number

    def get_grades(self):
        return self.__grades

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            print("Invalid grade")

    def calculate_average(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        return 0

    def display_student_info(self):
        print(f"Name: {self.__name}")
        print(f"Roll Number: {self.__roll_number}")
        print(f"Grades: {self.__grades}")
        print(f"Average Grade: {self.calculate_average():.2f}")


    name = property(get_name)
    roll_number = property(get_roll_number)
    grades = property(get_grades)

student = Student("John Doe", 53)
student.add_grade(88)
student.add_grade(45)
student.add_grade(78)

student.display_student_info()
