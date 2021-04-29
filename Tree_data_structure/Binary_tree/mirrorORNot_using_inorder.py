class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root, v):
    if root is None:
        return None
    else:
        inorder(root.left, v)
        v.append(root.data)
        inorder(root.right, v)


def mirrorUsingInorder(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    v1 = []
    v2 = []
    inorder(root1, v1)
    inorder(root2, v2)

    if len(v1) != len(v2):
        return False

    # Comparing the two arrays, if they
    # are reverse then return 1, else 0
    i = 0
    j = len(v2) - 1

    while j >= 0:

        if v1[i] != v2[j]:
            return False
        i += 1
        j -= 1

    return True


# tree 1
tree1 = Node(1)
tree1.left = Node(2)
tree1.right = Node(3)

# tree 2
tree2 = Node(1)
tree2.left = Node(3)
tree2.right = Node(2)

result = mirrorUsingInorder(tree1, tree2)
if result:
    print('it is a mirror tree')
else:
    print('it is not a mirror tree')
