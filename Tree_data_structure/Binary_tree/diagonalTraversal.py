class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diagonalTraversal(root):
    node = root
    q = []
    while node:
        print(node.data, end=' ')

        if node.left:
            q.append(node.left)

        if node.right:
            node = node.right

        else:
            if len(q):
                node = q.pop(0)
            else:
                node = None
    return


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
diagonalTraversal(tree)
