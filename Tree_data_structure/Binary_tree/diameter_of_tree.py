import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameter(root):
    if root is None:
        return 0
    else:
        ans = [-sys.maxsize]
        height(root, ans)
        return ans[0]


def height(root, ans):
    if root is None:
        return 0
    else:
        left_height = height(root.left, ans)
        right_height = height(root.right, ans)

        ans[0] = max(ans[0], 1 + left_height + right_height)

        return 1 + max(left_height, right_height)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
print('the diameter of the tree is : ', diameter(tree))
tree2 = Node(1)
tree2.left = Node(2)
tree2.left.right = Node(3)
tree2.left.right.right = Node(4)
tree2.left.right.right.left = Node(5)
tree2.right = Node(6)
tree2.right.left = Node(7)
print('the diameter of the tree2 is:', diameter(tree2))
tree3 = Node(1)
tree3.left = Node(2)
tree3.left.left = Node(4)
tree3.left.right = Node(5)
tree3.right = Node(3)
tree3.right.left = Node(6)
tree3.right.right = Node(7)
print('the diameter of the tree3 is:', diameter(tree3))
