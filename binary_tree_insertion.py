class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



    def insertion(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertion(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertion(data)
        else:
            self.data = Node(data)

    def preorder(self, start):
        if start is None:
            return
        print(start.data)
        self.preorder(start.left)
        self.preorder(start.right)


tree = Node(7)
tree.insertion(4)
tree.insertion(8)
tree.insertion(56)
tree.insertion(2)
tree.insertion(6)
tree.insertion(78)
tree.preorder(tree)
