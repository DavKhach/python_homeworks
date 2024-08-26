def custom_range(start, end, step):
    current = start
    while (step > 0 and current < end) or (step < 0 and current > end):
        yield current
        current += step

print("Numbers from 0 to 5 with a step of 0.5:")
for number in custom_range(0, 5, 0.5):
    print(number)
