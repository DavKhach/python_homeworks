numbers = range(1, 51)

even_numbers_generator = (num for num in numbers if num % 2 == 0)

print("Even numbers from 1 to 50:")
for even_number in even_numbers_generator:
    print(even_number)
