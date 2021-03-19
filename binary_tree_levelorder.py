class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if len(self.items):
            return self.items.pop(0)

    def peek(self):
        if len(self.items):
            return self.items[0].data


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)


    def levelOrder(self, start):

        queue = Queue()
        queue.enqueue(start)
        traversal = []

        while len(queue.items) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()

            if node.left is not None:
                queue.enqueue(node.left)

            if node.right is not None:
                queue.enqueue(node.right)

        return traversal




tree = BinaryTree(3)
tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)
tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)
print(tree.levelOrder(tree.root))
