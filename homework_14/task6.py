def min_max(lst):
    if not lst:
        return None, None

    min_element = lst[0]
    max_element = lst[0]

    for element in lst:
        if element < min_element:
            min_element = element
        if element > max_element:
            max_element = element

    return min_element, max_element

ls = [1, 4, 5, 9, 2, 4, 6, 9, 7]
min_element, max_element = min_max(ls)

print(f"The smallest element: {min_element}")
print(f"The largest element: {max_element}")
