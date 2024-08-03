def make_accumulator(start=0):
    total = start

    def accumulator(value):
        nonlocal total;
        total += value
        return total

    return accumulator

acc = make_accumulator(10)

print(acc(5))
print(acc(3))
print(acc(-2))
