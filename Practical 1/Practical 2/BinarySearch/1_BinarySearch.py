def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low<= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


n = int(input("Enter the size of the sorted array: "))

arr = list(map(int, input("Enter the elements of the sorted array: ").split()))

key = int(input("Enter the element to search for: "))

index = binary_search(arr, key)

if index != -1:
    print(f"Element {key} found at index {index}.")
else:
    print(f"Element {key} not found in the array.")


"""
TC: O(log n)
SC: O(1)

"""