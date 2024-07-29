def get_nth_element(iterable, n):
    it = iter(iterable)

    try:
        for _ in range(n):
            next(it)
        return next(it)
    except StopIteration:
        raise IndexError("The iterable is shorter than the requested index")

nums = [1, 2, 3, 4, 5]
print(get_nth_element(nums, 3))
print(get_nth_element(nums, 6))
