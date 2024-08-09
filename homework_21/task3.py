def validate_pos_int(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not (type(arg) == int and arg > 0):
                raise ValueError(f"Argument {arg} is not a positive integer")


        for key, value in kwargs.items():
            if not (type(value) == int and value > 0):
                raise ValueError(f"Argument {key}={value} is not a positive integer")

        return func(*args, **kwargs)

    return wrapper


@validate_pos_int
def multiply(a, b):
    return a * b


try:
    multiply(5, -2)
except ValueError as e:
    print(e)
