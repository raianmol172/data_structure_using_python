def mergeSort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left_result = mergeSort(left)
    right_result = mergeSort(right)

    return merge(left_result, right_result)


def merge(left_result, right_result):
    result = [None] * (len(left_result) + len(right_result))
    i = j = k = 0
    while i < len(left_result) and j < len(right_result):
        if left_result[i] <= right_result[j]:
            result[k] = left_result[i]
            i += 1
        else:
            result[k] = right_result[j]
            j += 1
        k += 1

    while i < len(left_result):
        result[k] = left_result[i]
        i += 1
        k += 1

    while j < len(right_result):
        result[k] = right_result[j]
        j += 1
        k += 1

    return result


arr = [50, 40, 30, 20, 10]
print(arr)
print('sorted array:')
print(mergeSort(arr))

