from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorderIterative(root):
    stack = deque()
    stack.append(root)
    curr = root

    while stack:
        if curr:
            print(curr.data, end=' ')
            if curr.right:
                stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()


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
print('preorder iterative: ')
preorderIterative(tree)
print('\npreorder recursive: ')
preorderRecursive(tree)
