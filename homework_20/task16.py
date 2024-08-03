import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_square(side):
    return side ** 2

def area_rectangle(width, height):
    return width * height

def area_triangle(base, height):
    return 0.5 * base * height


area_operations = {
    'circle': area_circle,
    'square': area_square,
    'rectangle': area_rectangle,
    'triangle': area_triangle
}


def calculate_area(shape, **kwargs):
    if shape not in area_operations:
        raise ValueError("Invalid shape")
    
    area_func = area_operations[shape]

    return area_func(**kwargs)


print(calculate_area('circle', radius=5))
print(calculate_area('square', side=4))
print(calculate_area('rectangle', width=3, height=5))
print(calculate_area('triangle', base=6, height=4))
