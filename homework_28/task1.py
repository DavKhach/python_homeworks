def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bubble_sort(ls)
print(f"Sorted list: {ls}")


"""
Time Complexity:
Best case: O(n) would be when array is already sorted, so swaps would be made.

Worst Case and Average Case: O(n**2)

Space Complexity:
O(1) In-place sorting, only a few extra variables are used
"""