def sort012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high = high - 1
    return arr


arr1 = [0, 2, 1, 0, 2, 1, 2, 0, 1, 0, 2]
print("before sorting:", arr1)
sort012(arr1)
print("after sorting:", arr1)
