def fibonacci_sequence(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, num):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


print(fibonacci_sequence(8))
