def func():
    nums = [1, 2, 3, 4, 5]

    iterator = iter(nums)

    try:
        while True:
            item = next(iterator)
            print(item)
    except StopIteration:
        print("Iteration complete")

func()
