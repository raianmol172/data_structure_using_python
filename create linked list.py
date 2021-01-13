# we had created a node here which has data and a pointer which points towards none for now
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
        while temp is not None:
            print(temp.data)
            temp = temp.next


# we have created the list here
l1 = Linked_list()
l1.head = Node(100)
l2 = Node(200)
l3 = Node(300)
l4 = Node(400)
# we have link the list with each other
l1.head.next = l2
l2.next = l3
l3.next = l4
l1.printList()
