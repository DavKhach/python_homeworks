def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculate(operand1, operand2, operator):
    if operator not in operations:
        raise ValueError("Invalid operator. Supported operators are +, -, *, /.")
    
    operation = operations[operator]
    
    return operation(operand1, operand2)


print(calculate(10, 5, '+'))
print(calculate(10, 5, '-'))
print(calculate(10, 5, '*'))
print(calculate(10, 5, '/'))


try:
    print(calculate(10, 0, '/'))
except ValueError as e:
    print(e) 
