from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorderIterative(root):
    stack = deque()
    stack.append(root)
    while stack:
        temp = stack.pop()
        print(temp.data, end=' ')
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)


def preorderRecursive(root):
    if root is None:
        return None
    else:
        print(root.data, end=' ')
        preorderRecursive(root.left)
        preorderRecursive(root.right)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
print('preorder iterative: ')
preorderIterative(tree)
print('\npreorder recursive: ')
preorderRecursive(tree)
