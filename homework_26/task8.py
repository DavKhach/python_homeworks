class PasswordValidator:
    def __init__(self, min_length=8, must_contain_number=True):
        self.min_length = min_length
        self.must_contain_number = must_contain_number
        self.__password = None

    def __get__(self, instance, owner):
        return self.__password

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Password must be string")

        if len(value) < self.min_length:
            raise ValueError(f"Password must be at least {self.min_length} long")

        if self.must_contain_number and not any(letter.isdigit() for letter in value):
            raise ValueError(f"Password must contain at least one number")

        self.__password = value

class Account:
    password = PasswordValidator(min_length=8, must_contain_number=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

try:
    account = Account("user", "password1")
    print(f"Username: {account.username}, Password: {account.password}")

    account.password = "passsssssss"
except ValueError as e:
    print(e)
