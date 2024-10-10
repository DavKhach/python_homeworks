def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

ls = [68, 24, 76, 13, 89, 53]
selection_sort(ls)
print(f"Sorted list: {ls}")


"""
Time Complexity:
Worst Case: O(n**2) algorithm will always perform n(n-1)/2 comparison
Best Case: O(n**2) Even if array is already sorted, the algorithm will still
perform all comparisons
Average Case: O(n**2)

Space Complexity: O(1) In-place sorting, only a few extra variables are used
"""