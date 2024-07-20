def sorted(lst):
    if len(lst) <= 1:
        return True

    if lst[0] > lst[1]:
        return False

    return sorted(lst[1:])

ls = [2, 6, 8, 10]
print(sorted(ls))
