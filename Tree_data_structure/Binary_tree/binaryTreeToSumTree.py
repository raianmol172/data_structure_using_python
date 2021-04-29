class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def toSumTree(root):
    # Base case
    if root is None:
        return 0

    # Store the old value
    old_val = root.data

    root.data = toSumTree(root.left) + toSumTree(root.right)

    return root.data + old_val


def inorder(root):
    if root is None:
        return None
    else:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
print('the inorder traversal of tree is: ')
inorder(tree)
result = toSumTree(tree)
print(' \n the inorder traversal of the new sumTree')
inorder(tree)
