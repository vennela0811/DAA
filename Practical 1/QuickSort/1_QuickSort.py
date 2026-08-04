def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def print_array(arr):
    print(*arr)


n = int(input("Enter the size of the array: "))

arr = list(map(int, input("Enter the elements of the array: ").split()))

print("\nOriginal array:", end=" ")
print_array(arr)

quick_sort(arr, 0, n - 1)

print("\nSorted array:", end=" ")
print_array(arr)

"""
TC: O(n log n) on average, O(n^2) in the worst case
SC: O(log n) due to recursion stack

"""