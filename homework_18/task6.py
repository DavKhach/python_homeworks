def apply_function(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))

    return result

def to_uppercase(s):
    return s.upper()

words = ["hello", "world", "bye"]
upper_words = apply_function(to_uppercase, words)
print(upper_words)
