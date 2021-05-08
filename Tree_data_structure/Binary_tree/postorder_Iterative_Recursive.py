from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorderIterative(root):
    stack1 = deque()
    stack1.append(root)
    stack2 = deque()
    while stack1:
        curr = stack1.pop()
        stack2.append(curr)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    while stack2:
        curr = stack2.pop()
        print(curr.data, end=' ')


def postorderRecursive(root):
    if root is None:
        return None
    else:
        postorderRecursive(root.left)
        postorderRecursive(root.right)
        print(root.data, end=' ')


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
print('postorder iterative: ')
postorderIterative(tree)
print('\npostorder recursive: ')
postorderRecursive(tree)
