def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        last = i - 1

        while last >= 0 and key < arr[last]:
            arr[last + 1] = arr[last]
            last = last - 1
        arr[last + 1] = key
        print(arr)


arr = [50, 40, 30, 20, 10]
insertionSort(arr)
print(arr)