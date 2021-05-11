class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLeaves(root):
    if root:
        printLeaves(root.left)
        if root.left is None and root.right is None:
            print(root.data, end=' ')
        printLeaves(root.right)


def printLeft(root):
    if root:
        if root.left:
            print(root.data, end=' ')
            printLeft(root.left)
        elif root.right:
            print(root.data, end=' ')
            printLeft(root.right)


def printRight(root):
    if root:
        if root.right:
            printRight(root.right)
            print(root.data, end=' ')
        elif root.left:
            printRight(root.left)
            print(root.data, end=' ')


def boundaryTraversal(root):
    if root:
        print(root.data, end=' ')
        printLeft(root.left)
        printLeaves(root.left)
        printLeaves(root.right)
        printRight(root.right)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
print('the boundary traversal of the tree: ')
boundaryTraversal(tree)
