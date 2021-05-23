arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def reverseArray(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def printArr(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=' ')


print("before reversing the array: ")
printArr(arr1)
reverseArray(arr1)
print("\nafter reversing the array: ")
printArr(arr1)
