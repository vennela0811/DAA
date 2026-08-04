def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]



def print_array(arr):
    print(*arr)


n = int(input("Enter the size of the array: "))

arr = list(map(int, input("Enter the elements of the array: ").split()))

print("\nOriginal array:", end=" ")
print_array(arr)

selection_sort(arr)

print("\nSorted array:", end=" ")
print_array(arr)

