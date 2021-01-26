class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def length_Iterative(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1  # we can also write it like count += 1
            temp = temp.next
        return count

    def length_Recursive(self, node):
        if node is None:
            return 0
        return 1 + self.length_Recursive(node.next)

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


l1 = LinkedList()
l1.head = Node(10)
l2 = Node(20)
l3 = Node(30)
l4 = Node(40)
l1.head.next = l2
l2.next = l3
l3.next = l4
l1.printList()
print("the length of the linked list is :", l1.length_Iterative())
print("the length of the linked list is :", l1.length_Recursive(l1.head))