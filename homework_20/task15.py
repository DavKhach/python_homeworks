def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def to_title_case(s):
    return s.title()

def reverse_string(s):
    return s[::-1]


string_operations = {
    'uppercase': to_uppercase,
    'lowercase': to_lowercase,
    'titlecase': to_title_case,
    'reverse': reverse_string
}


def manipulate_string(s, operation):
    if operation not in string_operations:
        raise ValueError("Invalid operation")

    operation_func = string_operations[operation]

    return operation_func(s)

print(manipulate_string("hello world", 'uppercase'))
print(manipulate_string("HELLO WORLD", 'lowercase'))
print(manipulate_string("hello world", 'titlecase'))
print(manipulate_string("hello world", 'reverse'))
