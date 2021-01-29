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
            return
        curr = self.head
        new_node = Node(data)
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
        new_node.next = None
        return

    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        new_node = Node(data)
        if curr:
            new_node.next = curr
            curr.prev = new_node
            self.head = new_node
            return

    def delete_node(self, node):
        curr = self.head
        while curr:
            if curr == node and curr == self.head:
                if not curr.next:
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
            elif curr == node:
                if curr.next is not None:
                    prev = curr.prev
                    nxt = curr.next
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

    def delete_Duplicates(self):
        curr = self.head
        dup_values = dict()
        while curr:
            if curr.data not in dup_values:
                dup_values[curr.data] = 1
                curr = curr.next

            else:
                nxt = curr.next
                self.delete_node(curr)
                curr = nxt


d1 = DoublyLinkedList()
d1.append(100)
d1.append(200)
d1.append(200)
d1.append(300)
d1.append(500)
d1.append(100)
d1.append(400)
d1.append(500)


d1.delete_Duplicates()
d1.printList()