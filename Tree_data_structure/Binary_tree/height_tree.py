class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):

    if root is None:
        return 0

    else:

        return 1 + max(height(root.left), height(root.right))


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
print('the height of the tree: ')
print(height(tree))

