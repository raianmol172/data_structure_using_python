def selectionSort(arr):
    for i in range(len(arr) - 1):
        min_val = i
        for item in range(i + 1, len(arr)):
            if arr[item] < arr[min_val]:
                min_val = item
        arr[i], arr[min_val] = arr[min_val], arr[i]
        print(arr)


arr = [10, 50, 3, 60, 1]
selectionSort(arr)

print(arr)
