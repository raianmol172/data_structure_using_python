def rotateArray(arr):
    n = len(arr) - 1
    x = arr[n]

    for i in range(n, 0, -1):

        arr[i] = arr[i - 1]

    arr[0] = x


arr1 = [1, 2, 3, 4, 5]
print("before rotating the array: \n", arr1)
rotateArray(arr1)
print("after rotating the array by one: \n", arr1)
