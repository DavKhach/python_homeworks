def compose(f, g):
    return lambda x: f(g(x))

def add_two(n):
    return n + 2

def square(n):
    return n * n

composed = compose(square, add_two)

print(composed(3))
