class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkDup(root):
    s = set()
    return helper(root, s)


def helper(root, s):
    if root is None:
        return False

    if root.data in s:
        return True

    s.add(root.data)

    return helper(root.left, s) or helper(root.right, s)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(1)
result = checkDup(tree)
if result:
    print('the tree have duplicates')
else:
    print('the tree does not have duplicates')
