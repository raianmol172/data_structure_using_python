def bubbleSort(arr):
    for iter in range(len(arr) - 1):
        for index in range(0, len(arr) - 1 - iter):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
        print(arr)


arr = [50, 40, 30, 20, 10]
bubbleSort(arr)

print(arr)
