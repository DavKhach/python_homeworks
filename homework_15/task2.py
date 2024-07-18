def nums(x):
    if x <= 0:
        return
    
    print(x)
    nums(x-1)

nums(5)
