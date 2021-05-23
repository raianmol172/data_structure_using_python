def bubbleSort(arr):
    for itr in range(len(arr) - 1):
        for index in range(0, len(arr) - 1 - itr):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
        print(arr)


arr1 = [50, 40, 30, 20, 10]
bubbleSort(arr1)

print(arr1)
