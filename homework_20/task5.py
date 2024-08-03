def power_factory(n):
    def power(x):
        return x ** n
    return power

square = power_factory(2)
cube = power_factory(3)

print(square(5))
print(cube(3))
