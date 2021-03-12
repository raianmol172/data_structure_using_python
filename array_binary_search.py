def binarySearch(my_array, target):
    left = 0
    right = len(my_array) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = my_array[middle]

        if target == middle_element:
            return middle

        elif target < middle_element:
            right = middle + 1

        else:
            left = middle - 1
    return -1


print(binarySearch([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 70))
