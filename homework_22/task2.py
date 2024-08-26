def prime_generator(n):
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

print("Prime numbers less than 100: ")
for prime in prime_generator(100):
    print(prime)
