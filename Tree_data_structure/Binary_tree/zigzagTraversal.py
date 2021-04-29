class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def zigzagTraversal(root):
    if root is None:
        return None

    else:

        stack1 = [root]
        stack2 = []
        itr = True

        while len(stack1):
            temp = stack1.pop(-1)
            print(temp.data, end=' ')

            if itr:
                if temp.left:
                    stack2.append(temp.left)
                if temp.right:
                    stack2.append(temp.right)
            else:
                if temp.right:
                    stack2.append(temp.right)
                if temp.left:
                    stack2.append(temp.left)

            if len(stack1) == 0:
                itr = not itr
                stack1, stack2 = stack2, stack1


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
print('the zigzag traversal of the tree is:')
zigzagTraversal(tree)

