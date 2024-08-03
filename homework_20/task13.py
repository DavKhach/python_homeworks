def bar(n):
    def make_multiplier(i):
        def multiplier(x):
            return x * i
        return multiplier

    return [make_multiplier(i) for i in range(n)]


functions = bar(5)

for i, func in enumerate(functions):
    print(f"Function {i}:")
    print(f"  Result of func(10): {func(10)}")
    print(f"  Closure attributes: {func.__closure__}")
    print()


