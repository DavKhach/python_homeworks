def infinite_sequence():
    num = 1
    while True:
        yield num
        num += 1

generator = infinite_sequence()
print("First 10 numbers from the infinite sequence: ")
for _ in range(10):
    print(next(generator))
