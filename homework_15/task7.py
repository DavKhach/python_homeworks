def str(x):
    if x == "":
        return x
    else:
        return str(x[1:]) + x[0]


print(str("hello"))

