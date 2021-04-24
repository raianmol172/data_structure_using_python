class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bottom_view(root):

    if root is None:
        return None

    else:
        q = [root]
        m = dict()
        hd = 0
        root.hd = hd
        while len(q):
            temp = q.pop(0)
            hd = temp.hd
            m[hd] = temp.data
            if temp.left:
                temp.left.hd = hd - 1
                q.append(temp.left)
            if temp.right:
                temp.right.hd = hd + 1
                q.append(temp.right)
        for i in sorted(m.keys()):
                print(m[i], end=' ')



tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
print('bottom view of the tree: ')
bottom_view(tree)
