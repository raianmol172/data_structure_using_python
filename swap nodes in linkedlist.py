class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def swap_node(self, key_1, key_2):
        if key_1 == key_2:
            return
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        if not curr_1 or not curr_2:
            return
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        curr_1.next, curr_2.next = curr_2.next, curr_1.next


if __name__ == '__main__':
    list1 = Linkedlist()
    list1.head = Node("mon")
    l2 = Node("tue")
    l3 = Node("wed")
    list1.head.next = l2
    l2.next = l3
    list1.printList()
    list1.swap_node("mon", "tue")
    print(" After swapping nodes: ")
    list1.printList()
