
def linearSearch(my_array, target):
    for i in range(len(my_array)):
        if my_array[i] == target:
            return i
    return False


my_array = [10, 20, 30, 40, 50]
print(linearSearch(my_array, 50))
