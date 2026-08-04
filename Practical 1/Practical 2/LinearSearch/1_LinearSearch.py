def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

n = int(input("Enter the size of the array: "))

arr = list(map(int, input("Enter the elements of the array: ").split()))

key = int(input("Enter the element to search for: "))

index = linear_search(arr, key)

if index != -1:
    print(f"Element {key} found at index {index}.")
else:
    print(f"Element {key} not found in the array.")



"""
TC: O(n)
SC: O(1)

"""