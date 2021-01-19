class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if self.is_empty() is not None:
            return self.items[-1]

    def getStack(self):
        return self.items


mystack = Stack()
mystack.push(10)
mystack.push('mon')
mystack.push(20)
mystack.pop()
print(mystack.getStack())
print(mystack.peek())
print(mystack.is_empty())