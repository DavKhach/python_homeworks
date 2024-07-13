def find_upper(string):
    for letter in string:
        if letter.isupper():
            return letter
    return None

str = "hello World"
result = find_upper(str)

if result:
    print(f"First uppercase letter is: {result}")
else:
    print("No uppercase letter found")
