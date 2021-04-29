class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBalanced(root):

    if root is None:
        return 0

    lh = isBalanced(root.left)
    rh = isBalanced(root.right)
    # checking if the subtree is ever false then returning
    # false for the whole recursion
    if lh is False or rh is False:
        return False
    if abs(lh-rh) > 1:
        # returning false if subtree is not balanced
        return False
    else:
        # returning height if subtree is balanced
        return max(lh, rh)+1


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
result = isBalanced(tree)
if result:
    print('the tree is balanced')
else:
    print('the tree is not balanced')
