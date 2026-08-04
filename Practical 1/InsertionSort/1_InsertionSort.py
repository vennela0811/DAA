def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key



def print_array(arr):
    print(*arr)


n = int(input("Enter the size of the array: "))

arr = list(map(int, input("Enter the elements of the array: ").split()))

print("\nOriginal array:", end=" ")
print_array(arr)

insertion_sort(arr)

print("\nSorted array:", end=" ")
print_array(arr)

"""
TC: O(n^2)
SC: O(1)

"""