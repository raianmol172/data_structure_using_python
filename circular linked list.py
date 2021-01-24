class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        temp = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break


if __name__ == '__main__':

    clist = CircularLinkedList()
    clist.append("C")
    clist.append("D")
    clist.prepend("B")
    clist.prepend("A")
    clist.append("E")
    clist.printList()

