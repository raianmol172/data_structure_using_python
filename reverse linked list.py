class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# 10 -> 20 -> 30 -> 40
# 40 -> 30 -> 20 -> 10
# 10 <- 20 <- 30 <- 40
    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev


l1 = LinkedList()
l1.head = Node(10)
l2 = Node(20)
l3 = Node(30)
l4 = Node(40)
l1.head.next = l2
l2.next = l3
l3.next = l4
print("before reversing the nodes")
l1.printList()
l1.reverse_iterative()
print("after reversing the nodes")
l1.printList()
