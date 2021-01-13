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
l1.head = Node('Anmol')
l2 = Node('Manish')
l3 = Node('Abhishek')
l4 = Node('Aayush')
l5 = Node('chimmo')
l1.head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
print("before deletion: ")
l1.printList()
print("after deletion")
l1.deleteNode('Anmol')
l1.deleteNode('Aayush')
l1.deleteNode('karan')
l1.printList()
