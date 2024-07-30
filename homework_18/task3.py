def my_zip(*iterables: list) -> list:
    """
    The function has *iterables as his argument which means that
    my_zip accepts arbitrary number of positional arguments

    In the end my_zip returns a list of tuples, where each
    tuple contains elements from the iterables at the corresponding position
    """
    min_length = min(len(iterable) for iterable in iterables)

    result = []
    for i in range(min_length):
        new_tuple = tuple(iterable[i] for iterable in iterables)
        result.append(new_tuple)

    return result

ls1 = [1, 2, 3]
ls2 = ['a', 'b', 'c']
ls3 = [True, False, False]

zipped = my_zip(ls1, ls2, ls3)
print(zipped)
