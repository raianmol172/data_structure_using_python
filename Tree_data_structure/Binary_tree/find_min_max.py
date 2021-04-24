class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findMaximum(root):

    if root is None:
        return 0

    else:

        maximum = root.data
        if root.left:
            left_max = findMaximum(root.left)
            maximum = max(maximum, left_max)

        if root.right:
            right_max = findMaximum(root.right)
            maximum = max(maximum, right_max)

        return maximum


def findMinimum(root):

    if root is None:
        return 0

    else:

        minimum = root.data

        if root.left:
            left_min = findMinimum(root.left)
            minimum = min(minimum, left_min)

        if root.right:
            right_min = findMinimum(root.right)
            minimum = min(minimum, right_min)

        return minimum



tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
print('the maximum nodes value is: ')
print(findMaximum(tree))
print('the minimum nodes value is: ')
print(findMinimum(tree))
