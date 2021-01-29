class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
            self.head.next = None
            return
        curr = self.head
        new_node = Node(data)
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
        new_node.next = None

    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        new_node = Node(data)
        if curr:
            curr.prev = new_node
            new_node.next = curr
            new_node.prev = None
            self.head = new_node

    def delete(self, key):
        curr = self.head
        while curr:
            if curr.data == key and curr == self.head:
                if curr.next is None:
                    curr = None
                    self.head = None
                    return
                else:
                    nxt = curr.next
                    self.head = nxt
                    nxt.prev = None
                    curr.next = None
                    curr = None
                    return

            elif curr.data == key:
                if curr.next is not None:
                    nxt = curr.next
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr.next = None
                    curr.prev = None
                    curr = None
                    return

                else:
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return

            curr = curr.next


d1 = DoublyLinkedList()
d1.prepend(100)
d1.append(200)
d1.append(300)
d1.append(400)
d1.delete(400)
d1.printList()