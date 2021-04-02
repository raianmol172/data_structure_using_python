# two sum is a problem where we need to find the pair which sum up to some particular value let say 7
# here we use hash table for solving these problem which make its complexity O(n)

def twoSum(arr, target):
    store = {}  # dictionary hash table
    for i in range(len(arr)):
        if arr[i] in store:
            return [store[arr[i]], i]
        else:
            store[target - arr[i]] = i


arr = [1, 2, 6, 3, 9]
print(twoSum(arr, 7))
