def BinarySearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2  
        if arr[mid] == x:
            return mid 
        elif arr[mid] < x:
            low = mid + 1  
        else:
            high = mid - 1  
    return -1  
arr = []
n = int(input("Enter size of array: "))
print("Enter elements in sorted order:")
for i in range(n):
    k = int(input(f"Element {i + 1}: "))
    arr.append(k)
print("Array:", arr)

x = int(input("Enter target element: "))
result = BinarySearch(arr, 0, n - 1, x)
if result != -1:
    print(f"Element {x} is present at index {result}.")
else:
    print(f"Element {x} is not present in the array.")
