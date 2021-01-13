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

        while temp == None:
            return

        prev.next = temp.next
        temp = None

l1= LinkedList()
l1.head = Node('sunday')
l2 = Node('monday')
l3 = Node('tuesday')
l4 = Node('wednesday')
l5 = Node('thursday')
l1.head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
print("Before deletion")
l1.printList()
print("After deletion")
l1.deleteNode('monday')
l1.printList()