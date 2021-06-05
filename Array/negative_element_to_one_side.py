def shiftNegative(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] > 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] > 0 and arr[right] > 0:
            right -= 1
        elif arr[left] < 0 and arr[right] > 0:
            left += 1
            right -= 1
        else:
            left += 1

    return arr


arr1 = [-1, 3, 6, -2, -9]
shiftNegative(arr1)
print(arr1)