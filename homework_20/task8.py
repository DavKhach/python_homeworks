def make_greeting(greeting):
    def greet(name):
        print(f"{greeting} {name}")

    return greet

greet_hello = make_greeting("Hello")
greet_hello("Alice")
