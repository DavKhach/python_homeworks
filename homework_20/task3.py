def apply_twice(f, x):
    return f(f(x))

def square(n):
    return n * n

print(apply_twice(square, 2))
