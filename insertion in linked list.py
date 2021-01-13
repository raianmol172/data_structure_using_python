class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):  # this is a function to insert data at starting position
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):  # this is a function to insert data at the end
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insert(self, prev_node, new_data):  # this is a position to insert at a given position
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def printList(self):   #  this function simply print list
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

l1 = Linkedlist()
l1.head = Node(1)
l2 = Node(2)
l3 = Node(3)
l1.head.next = l2
l2.next = l3
print("Before insertion: ")
l1.printList()
l1.push(100)
l1.append(200)
l1.insert(l2, 1000)
l1.append('monday')
l1.push('sunday')
print("After insertion: ")
l1.printList()