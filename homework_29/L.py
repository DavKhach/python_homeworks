"""Bad Example"""

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#
# rect = Rectangle(2, 5)
# sq = Square(5)
#
# print(rect.area())
# print(sq.area())

"""The Square class alters behavior of Rectangle, violating LSP because a
Square is not a true Rectangle"""


"""Right example"""

class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

rect = Rectangle(2, 5)
sq = Square(5)

print(rect.area())
print(sq.area())

"""Both Square and Rectangle now inherit from Shape class, and they implement 
their own area() methods correctly without interfering with each other"""
