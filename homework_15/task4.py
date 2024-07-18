def natural_nums(x):
    if x <= 1:
        return x

    return x + natural_nums(x-1)

print(natural_nums(10))
