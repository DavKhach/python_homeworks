def sort_list(lst):
    return sorted(lst)

def reverse_list(lst):
    return lst[::-1]

def filter_list(lst, condition):
    return [x for x in lst if condition(x)]

def map_list(lst, transform):
    return [transform(x) for x in lst]


list_transformations = {
    'sort': sort_list,
    'reverse': reverse_list,
    'filter': filter_list,
    'map': map_list
}


def transform_list(lst, operation, *args):
    if operation not in list_transformations:
        raise ValueError("Invalid operation")

    transform_func = list_transformations[operation]

    return transform_func(lst, *args)


lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]


print(transform_list(lst, 'sort'))
print(transform_list(lst, 'reverse'))
print(transform_list(lst, 'filter', lambda x: x % 2 == 0))
print(transform_list(lst, 'map', lambda x: x ** 2))
