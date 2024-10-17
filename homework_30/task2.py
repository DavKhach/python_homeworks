class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}: {self.age} years"

def insertion_sort(arr, key):
    for  i in range(1, len(arr)):
        other = arr[i]
        j = i-1
        while j >= 0 and getattr(arr[j], key) > getattr(other, key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = other
    return arr

students = [Student("John", 20),
            Student("Alice", 18),
            Student("Bob", 32),
            Student("Arnold", 20),
            Student("Tom", 27)]


sort_stud = insertion_sort(students, key="age")
print(sort_stud)
