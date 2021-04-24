class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def left_view(root):

    if root is None:
        return None

    else:
        q = [root]

        while len(q):
            for i in range(1, len(q) + 1):   # when the value of i==1 then print the popped node
                temp = q.pop(0)
                if i == 1:
                    print(temp.data, end=' ')
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)



def right_view(root):

    if root is None:
        return None

    else:
        q = [root]

        while len(q):
            for i in range(1, len(q) + 1):   # when the value of i==1 then print the popped node
                temp = q.pop(0)
                if i == 1:
                    print(temp.data, end=' ')
                if temp.right:
                    q.append(temp.right)
                if temp.left:
                    q.append(temp.left)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
print('left view of the tree: ')
left_view(tree)
print('\n right view of the tree: ')
right_view(tree)
