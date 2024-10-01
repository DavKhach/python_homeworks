class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Width must be positive")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Height must be positive")
        self.__height = value

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return (self.width + self.height) * 2

try:
    rect = Rectangle(5, 10)
    print(f"Area : {rect.area}")
    print(f"Perimeter : {rect.perimeter}")

    rect.width = 7
    print(f"New area: {rect.area}")
    print(f"New perimeter: {rect.perimeter}")
except ValueError as e:
    print(e)
