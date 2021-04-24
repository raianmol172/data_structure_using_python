class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelOrderTraversal(root):

    if root is None:
        return None

    else:

        q = [root]

        while len(q):
            temp = q.pop(0)
            print(temp.data, end=' ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
print('level order traversal: ')
levelOrderTraversal(tree)


