def make_adder(n):
    return lambda x: x + n

add_5 = make_adder(5)
add_10 = make_adder(10)

print(add_5(2))
print(add_10(5))
