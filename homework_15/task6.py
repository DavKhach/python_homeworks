def length(x):
    if not x:
        return 0

    return length(x[1:]) + 1

print(length(["hello", 4, "world", 12, 65]))
