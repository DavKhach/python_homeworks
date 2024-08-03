def square(n):
    return n * n

def cube(n):
    return n * n * n

def square_root(n):
    return n ** 0.5

def factorial(n):
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


math_functions = {
    'square': square,
    'cube': cube,
    'square_root': square_root,
    'factorial': factorial
}


def math_operations(number, operation):
    if operation not in math_functions:
        raise ValueError("Invalid operation")
    
    math_func = math_functions[operation]
    
    return math_func(number)

number = 5

print(math_operations(number, 'square'))
print(math_operations(number, 'cube'))
print(math_operations(number, 'square_root'))
print(math_operations(number, 'factorial'))
