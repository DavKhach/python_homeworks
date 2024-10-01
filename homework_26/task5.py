class ValidatedString:
    def __init__(self, min_length):
        self.__min_length = min_length
        self.__value = None

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Value must be string")
        if len(value) < self.__min_length:
            raise ValueError(f"String must be at least {self.__min_length} long")
        self.__value = value

class User:
    username = ValidatedString(min_length=5)

    def __init__(self, username):
        self.username = username

try:
    user = User("JohnDoe")
    print(f"Username: {user.username}")

    user.username = "Tom"
except ValueError as e:
    print(e)
