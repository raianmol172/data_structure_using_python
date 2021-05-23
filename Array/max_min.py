arr1 = [1, 5, 3, 8, 10, -100]


def maxValue(arr):
    max_val = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val


def minValue(arr):
    min_val = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val


print("the maximum value is: ", maxValue(arr1))
print("the minimum value is: ", minValue(arr1))
