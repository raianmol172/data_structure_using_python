class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def preorder(self, start):
        if start is None:
            return
        print(start.data, end=' ')
        self.preorder(start.left)
        self.preorder(start.right)

    def inorder(self, start):
        if start is None:
            return
        self.inorder(start.left)
        print(start.data, end=' ')
        self.inorder(start.right)

    def postorder(self, start):
        if start is None:
            return
        self.postorder(start.left)
        self.postorder(start.right)
        print(start.data, end=' ')


tree = BinaryTree(3)
tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)
tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)
print('postorder traversal: ')
tree.preorder(tree.root)
print('\ninorder traversal: ')
tree.inorder(tree.root)
print('\npostorder traversal: ')
tree.postorder(tree.root)


