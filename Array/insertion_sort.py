def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        last = i - 1
        while last >= 0 and key < arr[last]:
            arr[last + 1] = arr[last]
            arr[last] = key
            last = last - 1
            print(arr)


arr1 = [5, 4, 3, 2, 1]
insertionSort(arr1)
print(arr1)
