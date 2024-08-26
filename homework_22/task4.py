squares_generator = (x**2 for x in range(1, 21))

print("Square of numbers from 1 to 20: ")
for square in squares_generator:
    print(square)
