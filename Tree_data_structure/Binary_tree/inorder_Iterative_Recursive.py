from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorderIterative(root):
    stack = deque()
    curr = root
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.data, end=' ')
            curr = curr.right


def inorderRecursive(root):
    if root is None:
        return None
    else:
        inorderIterative(root.left)
        print(root.data, end=' ')
        inorderIterative(root.right)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
print('inorder iterative: ')
inorderIterative(tree)
print('\ninorder recursive: ')
inorderRecursive(tree)
