def custom_reduce(func, iterable, initializer=None):
    it = iter(iterable)

    if initializer is None:
        try:
            accumulator = next(it)
        except StopIteration:
            raise TypeError("Reduce() of empty sequence with no initial value")
    else:
        accumulator = initializer

    if initializer is not None or not isinstance(accumulator, (list, tuple, dict)):
        yield accumulator

    for item in it:
        accumulator = func(accumulator, item)
        yield accumulator

numbers = [1, 2, 3, 4, 5]
lambda_add = lambda x, y: x + y

print("Intermediate results of custome_reduce:")
for result in custom_reduce(lambda_add, numbers):
    print(result)
