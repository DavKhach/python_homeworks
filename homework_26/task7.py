class RangeDescriptor:
    def __init__(self):
        self.__value = None

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be integer")
        if value < 1 or value > 1000:
            raise ValueError("Value must be between 1 and 100")
        self.__value = value

class Product:
    price = RangeDescriptor()

    def __init__(self, name, price):
        self.name = name
        self.price = price

try:
    product = Product("Laptop", 699)
    print(f"Product: {product.name}, Price: {product.price}$")

    product.price = 1200
except ValueError as e:
    print(e)
