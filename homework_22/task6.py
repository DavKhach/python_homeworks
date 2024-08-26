def repeat_element(element, times):
    for _ in range(times):
        yield element


print("Repeating 'A' 5 times: ")
for item in repeat_element('A', 5):
    print(item)


print("\nRepeating 42 three times:")
for item in repeat_element(42, 3):
    print(item)

print("\nRepeating [1, 2] twice")
for item in repeat_element([1, 2], 2):
    print(item)
