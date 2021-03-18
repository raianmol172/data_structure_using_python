def quickSort(arr):
    qshelper(arr, 0, len(arr) - 1)
    return arr


def qshelper(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while right >= left:

        if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
            arr[left], arr[right] = arr[right], arr[left]

        if arr[left] <= arr[pivot]:
            left += 1

        if arr[right] >= arr[pivot]:
            right -= 1

    arr[right], arr[pivot] = arr[pivot], arr[right]
    print(arr)
    qshelper(arr, start, right - 1)
    qshelper(arr, right + 1, end)


arr = [50, 40, 30, 20, 10]
print('steps of sorting:')
quickSort(arr)
print('After sorting :', arr)

