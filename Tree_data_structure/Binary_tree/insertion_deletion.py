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
    if not root:
        return Node(key)
    else:
        q = [root]
        while len(q):
            temp = q.pop(0)
            if temp.left is None:
                temp.left = Node(key)
                return
            else:
                q.append(temp.left)
            if temp.right is None:
                temp.right = Node(key)
                return
            else:
                q.append(temp.right)


def deletion(root, key):
    if not root:
        return None
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root
    else:
        key_node = None
        q = [root]
        while len(q):
            temp = q.pop(0)
            if temp.data == key:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node:
            x = temp.data
            deletionHelper(root, temp)
            key_node.data = x
            return root


def deletionHelper(root, d_node):
    q = [root]
    while len(q):
        temp = q.pop(0)
        if temp.data is d_node:
            temp.data = None
            return
        if temp.left is d_node:
            temp.left = None
            return
        else:
            q.append(temp.left)
        if temp.right is d_node:
            temp.right = None
            return
        else:
            q.append(temp.right)


tree = None
tree = insertion(tree, 1)
insertion(tree, 2)
insertion(tree, 3)
insertion(tree, 4)
insertion(tree, 5)
insertion(tree, 6)
insertion(tree, 7)
print('the inorder traversal of the tree: ')
inorderTraversal(tree)
print('\n After deletion: ')
deletion(tree, 2)
deletion(tree, 4)
inorderTraversal(tree)



