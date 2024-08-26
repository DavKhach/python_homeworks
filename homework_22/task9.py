def gen1():
    for i in range(1, 6):
        yield i


def gen2():
    yield from gen1()
    for i in range(6, 11):
        yield i


print("Values yielded by gen2():")
for value in gen2():
    print(value)
