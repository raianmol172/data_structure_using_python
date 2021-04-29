class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mirrorOrNot(root1, root2):

    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.data == root2.data and mirrorOrNot(root1.left, root2.right) \
            and mirrorOrNot(root1.right, root2.left):
        return True


# tree 1
tree1 = Node(1)
tree1.left = Node(2)
tree1.right = Node(3)

# tree 2
tree2 = Node(1)
tree2.left = Node(3)
tree2.right = Node(2)

result = mirrorOrNot(tree1, tree2)
if result:
    print('the trees are mirror')
else:
    print('the trees are not mirror')
