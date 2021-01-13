class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def deleteList(self):
        current = self.head
        while current is not None:
            temp = current.next
            del current.data
            current = temp


l1 = LinkedList()
l1.head = Node(10)
l2 = Node(20)
l3 = Node(30)
l1.head.next = l2
l2.next = l3
l1.printList()
print("deleting the list:")
l1.deleteList()
# l1.printList() this throws an error as we had delete the list

