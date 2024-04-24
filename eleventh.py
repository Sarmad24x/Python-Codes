def binarySearch(arr, element, low, high):
    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] == element:
            return mid

        elif arr[mid] < element:
            low = mid + 1

        else:
            high = mid - 1

    return -1


arr = [3, 4, 5, 6, 7, 8, 9]
element = 4

result = binarySearch(arr, element, 0, len(arr)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")