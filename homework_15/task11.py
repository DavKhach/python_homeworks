def sum(num):
    if num < 10:
        return num

    return num % 10 + sum(num // 10)

number = 51381
print(sum(number))
