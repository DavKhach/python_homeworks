def custom_map(func, iterable):
    for item in iterable:
        yield func(item)


numbers = [1, 2, 3, 4, 5]
square = lambda x: x ** 2

print("Squared numbers:")
for squared in custom_map(square, numbers):
    print(squared)
