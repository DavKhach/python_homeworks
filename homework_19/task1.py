def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

multi_of_3 = make_multiplier_of(3)
print(multi_of_3(10))

multi_of_10 = make_multiplier_of(10)
print(multi_of_10(5))
