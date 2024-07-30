def my_filter(func: callable, iterable: list) -> list:
    """
    We have two arguments in my_filter function:
    - func: A function that takes one argument and returns a boolen
    - iterable: A list of items to be filtered

    In the end my_filter returns a list of items for which the function returns True
    """

    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

def is_even(x: int) -> bool:
    return x % 2 == 0

nums = [1, 2, 3, 4, 5]
even_nums = my_filter(is_even, nums)
print(even_nums)
