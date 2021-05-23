def search(arr, n):
    for i in range(0, len(arr)):
        if arr[i] == n:
            return True
    return False


arr1 = [8, 4, 6, 2, 0]
print(search(arr1, 2))
