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
            print("  %s" %(temp.data))
            temp = temp.next

    def deleteNode(self, value):
        temp = self.head

        if temp.data == value:
            self.head = temp.next
            temp = None
            return

        while temp is not None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

l1 = LinkedList()
l1.head = Node('A')
l2 = Node('B')
l3 = Node('C')
l4 = Node('D')
l5 = Node('E')
l1.head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
print("before deletion: ")
l1.printList()
print("after deletion")
l1.deleteNode('A')
l1.deleteNode('C')
l1.deleteNode('E')
l1.printList()
