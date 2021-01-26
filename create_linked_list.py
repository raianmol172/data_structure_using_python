# we had created a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# here we have initialize the head

class Linked_list:

    def __init__(self):
        self.head = None

    def printList(self):  # the function that will print the list
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node


l1 = Linked_list()
l1.append(100)
l1.append(200)
l1.prepend(10)
l1.prepend(20)
l1.printList()
