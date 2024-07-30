def my_map(func: callable, iterable: list)-> list:
    """ 
    We have two arguments in my_map function:
    - func: A function that takes one argument and returns a result
    - iterable: A list of items to which the function will be applied

    In the end my_map returns a list of results after applying 
    the function to each item in the iterable
    """

    result = []
    for item in iterable:
        result.append(func(item))
    return result

def square(x: 'int'):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = my_map(square, nums)
print(squared_nums)
