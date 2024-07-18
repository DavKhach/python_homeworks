def ls_elem(lst):
    if not lst:
        return
    print(lst[0])
    ls_elem(lst[1:])

ls = [1,2,3,4,5]
ls_elem(ls)
