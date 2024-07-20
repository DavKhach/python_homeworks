def prime(num, divisor=2):
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % divisor == 0:
        return  False

    if divisor * divisor > num:
        return True

    return prime(num, divisor + 1)

print(prime(13))
