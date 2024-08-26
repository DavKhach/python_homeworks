def exception_propagator(iterable):
    for item in iterable:
        if item == "error":
            raise ValueError("An error occurred!")
        yield item

test_list = ["a", "b", "error", "c"]

try:
    for item in exception_propagator(test_list):
        print(item)
except ValueError as e:
    print(e)
