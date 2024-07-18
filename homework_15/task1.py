def nums(x):
    if x <= 0:
        return
    nums(x-1)
    print(x)

nums(5)
