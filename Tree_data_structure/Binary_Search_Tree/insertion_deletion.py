class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorderTraversal(root):
    if root is None:
        return None
    else:
        inorderTraversal(root.left)
        print(root.data, end=' ')
        inorderTraversal(root.right)


def insertion(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data < key:
            root.right = insertion(root.right, key)
        else:
            root.left = insertion(root.left, key)
        return root



def deletion(root, key):
    if not root:
        return None
    else:
        if root.data == key:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            else:
                temp = minValue(root.right)
                root.data = temp.data
                root.right = deletion(root.right, temp.data)
            return root
        if root.data < key:
            root.right = deletion(root.right, key)
        else:
            root.left = deletion(root.left, key)

        return root


def minValue(root):
    while root.left:
        root = root.left
    return root


tree = None
tree = insertion(tree, 2)
insertion(tree, 1)
insertion(tree, 3)
print('insertion: ')
inorderTraversal(tree)
deletion(tree, 1)
print(' \n after deletion: ')
inorderTraversal(tree)
