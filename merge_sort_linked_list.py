class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        new_node = Node(data)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return

    def sortedMerge(self, a, b):
        result = None

        if a == None:
            return b
        if b == None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result


    def mergeSort(self, head):

        if head == None or head.next == None:
            return head

        middle = self.getMiddle(head)
        nexttomiddle  = middle.next
        middle.next = None

        left = self.mergeSort(head)
        right = self.mergeSort(nexttomiddle)

        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def getMiddle(self, head):

        if head == None:
            return head

        slow = head
        fast = head

        while slow.next != None and slow.next.next != None:

            slow = slow.next
            fast = fast.next.next

        return slow


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end= " ")
            temp = temp.next
        print(' \n ')


l1 = LinkedList()
l1.append(40)
l1.append(30)
l1.append(20)
l1.append(10)
l1.printList()
l1.head = l1.mergeSort(l1.head)
print("after sorting linked list:")
l1.printList()
