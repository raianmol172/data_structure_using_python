class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        while index != 0:
            curr = curr.next
            index -= 1

        return curr.data

    def addAtHead(self, key):
        new_node = Node(key)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def addAtTail(self, key):
        new_node = Node(key)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node

        self.size += 1

    def addAtIndex(self, index, key):
        if index < 0 or index > self.size:
            return -1
        new_node = Node(key)
        if index == 0:
            self.addAtHead(key)
        elif index == self.size - 1:
            self.addAtTail(key)
        else:
            curr = self.head
            while index - 1 != 0:   # here we keep track on index - 1 so that we can add after that element
                curr = curr.next
                index -= 1
            curr.next = new_node
            new_node.next = curr.next
            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        if index == 0:
            self.head = curr.next
        elif index == self.size - 1:
            while index - 1 != 0:
                curr = curr.next
            curr.next = 0
            self.tail = curr
        else:
            while index != 0:
                prev = curr
                curr = curr.next
                index -= 1
            prev.next = curr.next
        self.size -= 1



myLinkedList = LinkedList()
myLinkedList.addAtIndex(0, 200)
myLinkedList.addAtIndex(1, 300)
myLinkedList.addAtIndex(2, 400)
myLinkedList.deleteAtIndex(1)
print(myLinkedList.get(1))
