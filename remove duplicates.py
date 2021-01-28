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

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

    def duplicate(self):
        prev = None
        curr = self.head
        dup_value = dict()
        while curr:
            if curr.data in dup_value:     
                prev.next = curr.next
                curr = None
            else:
                dup_value[curr.data] = 1
                prev = curr
            curr = prev.next



l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(10)
l1.prepend(100)
l1.prepend(20)
l1.prepend(30)
l1.prepend(10)
print("before removing duplicates")
l1.printList()
l1.duplicate()
print("after removing duplicates")
l1.printList()