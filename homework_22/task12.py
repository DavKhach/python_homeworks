def custom_zip(*iterables):
    iterators = [iter(it) for it in iterables]
    
    while True:
        try:
            result = tuple(next(it) for it in iterators)
            yield result
        except StopIteration:
            return

list1 = [1, 2, 3, 4]
list2 = ['a', 'b']
list3 = [True, False, True]

print("Results of custom_zip:")
for item in custom_zip(list1, list2, list3):
    print(item)
