def custom_filter(func, iterable):
    for item in iterable:
        if func(item):
            yield item

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_even = lambda x: x % 2 == 0

print("Filtered even numbers:")
for number in custom_filter(is_even, numbers):
    print(number)
