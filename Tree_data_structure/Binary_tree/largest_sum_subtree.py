import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def largestSumSubtree(root):
    if root is None:
        return 0
    ans = [-sys.maxsize]
    largestSumHelper(root, ans)
    return ans[0]


def largestSumHelper(root, ans):

    if root is None:
        return 0

    else:
        curr_sum = (root.data + largestSumHelper(root.left, ans) + largestSumHelper(root.right, ans))

        ans[0] = max(curr_sum, ans[0])

        return curr_sum



tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(3)
tree.left.right = Node(4)
tree.right.left = Node(-6)
tree.right.right = Node(-8)
print('the largest sum of subtree is: ')
print(largestSumSubtree(tree))

