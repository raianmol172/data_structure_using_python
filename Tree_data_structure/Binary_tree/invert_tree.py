class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorderTraversal(root):
    if root is None:
        return None
    else:
        print(root.data, end=' ')
        preorderTraversal(root.left)
        preorderTraversal(root.right)


def invertTree(root):

    if root is None:
        return None

    else:
        root.left, root.right = root.right, root.left

        root.left = invertTree(root.left)
        root.right = invertTree(root.right)

        return root


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
print('before inverting/mirror_image the tree: ')
preorderTraversal(tree)
invertTree(tree)
print('\n after inverting/mirror_image the tree: ')
preorderTraversal(tree)

