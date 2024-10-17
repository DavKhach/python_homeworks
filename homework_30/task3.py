import random, time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            continue
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


if __name__ == "__main__":
    nums = [random.randint(1, 100) for i in range(10000)]

    start = time.perf_counter()

    print(insertion_sort(nums))

    end = time.perf_counter()

    print(f"Before sort: {round(end-start, 6)} seconds")

    start = time.perf_counter()

    print(insertion_sort(nums))

    end = time.perf_counter()

    print(f"After sort: {round(end - start, 6)} seconds")
