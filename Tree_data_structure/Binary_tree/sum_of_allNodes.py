class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sumAllNode(root):

    if not root:
        return 0

    else:

        curr_sum = (root.data + sumAllNode(root.left) + sumAllNode(root.right))

    return curr_sum


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
print('sum of all the nodes in the tree: ')
print(sumAllNode(tree))
