# both the function will take O(n*log(n)) time

def kthMin(arr, k):

    # sort the array
    arr.sort()

    # return kth element in the sorted array
    return arr[k-1]


arr1 = [2, 4, 7, 1, 23, 13]

print(kthMin(arr1, k=1))


def kthMax(arr, k):

    # sort the given array in reverse
    arr.sort(reverse=True)

    # return the kth element from the array
    return arr[k-1]


arr2 = [1, 4, 2, 6, 9]
print(kthMax(arr2, k=2))
