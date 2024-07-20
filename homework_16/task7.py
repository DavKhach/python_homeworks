def power_of_two(num):
    if num <= 0:
        return False

    return num & (num - 1) == 0

print(power_of_two(32))
