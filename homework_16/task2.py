def sum_of_elements(lst):
    if not lst:
        return 0

    return lst[0] + sum_of_elements(lst[1:])

ls = [1, 2, 3, 4, 5]
print(sum_of_elements(ls))
