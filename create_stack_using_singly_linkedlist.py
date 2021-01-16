class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.head is None:
            self.head = Node(data)

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.isempty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        temp = self.head
        if self.isempty():
            return None
        else:
            while temp is not None:
                print(temp.data, "->", end=" ")
                temp = temp.next
            print("\n")
            return


if __name__ == '__main__':
    mystack = Stack()
    mystack.push(10)
    mystack.push(20)
    mystack.push(30)
    mystack.push(40)
    mystack.display()
    print("Top element is: ", mystack.peek())
    print("Removed element is ", mystack.pop())
    print("Removed element is ", mystack.pop())
    print("Top element is: ", mystack.peek())
    mystack.display()
    print(mystack.isempty())
    print("Removed element is ", mystack.pop())
    print("Removed element is ", mystack.pop())
    mystack.display()
    print(mystack.isempty())

