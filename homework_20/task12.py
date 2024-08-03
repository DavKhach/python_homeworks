def make_memoize(f):
    cache = {}

    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    
    return memoized

def slow_function(x):
    print(f"Computing {x}...")
    return x * x

memoized_function = make_memoize(slow_function)

print(memoized_function(4))
print(memoized_function(4))
print(memoized_function(5))
