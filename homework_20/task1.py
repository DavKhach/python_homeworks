multiplier = lambda factor: lambda x: x * factor

double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))
