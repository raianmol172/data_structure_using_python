def largestContiguous(arr):

    max_so_far = 0
    max_ending_here = 0

    for i in range(len(arr)):

        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    return max_so_far


arr1 = [-2, 3, -5, 6, 2]
arr2 = [2, -3, 4, -1, -2, 1, 5, -3]
print("the largest continuous sub-array is :", largestContiguous(arr2))
